import os
import time
import math
from celery import Celery 
import matplotlib.pyplot as plt
from parse import parse
from functions_base import funcdict
from mongoengine import connect
import numpy as np
from pandas import DataFrame 

from models import Column, Data



CELERY_BROKER_URL = os.environ.get('BROKER_URL', 'redis://localhost:6379'),
CELERY_RESULT_BACKEND = os.environ.get('RESULT_BACKEND', 'redis://localhost:6379')

celery = Celery('tasks', broker=CELERY_BROKER_URL, backend=CELERY_RESULT_BACKEND)

@celery.task(name='tasks.add')
def process(id,email,functions,columns):
    connect('datafactoring', host='mongo', port=27017, username='admin', password='admin')
    plt.subplots_adjust(wspace=2.2,hspace=2.2)
    result = []
    file = Data.objects().get(id=id).file.get()
    print(Data.objects().get(id=id).file)
    print(dir(Data.objects().get(id=id).file))
    data = parse(file)
    cols = []
    for k, v in data.items():
        cols.append(Column(name = k, data = v))
    data = [column for column in data if column.name in columns]
    for column in data:
        print(f"iter column: {column}")
        for function in functions:
            print(f"iter function: {function}")
            if isinstance(function,list):
                processed = [num for num in column['data'] if isinstance(num, (int, float))]
                names = []
                for subfunc in function:
                    func = funcdict[subfunc['name']]['func']
                    processed = func(inp=np.array(processed), **subfunc['args'])
                    names.append(subfunc['name'])
                result.append({
                    'name': ' '.join(names),
                    'column': column.name,
                    'data': processed
                })
            else :
                func = funcdict[function['name']]['func']
                arr = [num for num in column['data'] if isinstance(num, (int, float))]
                processed = func(inp=np.array(arr), **function['args'])
                result.append({
                    'name': function['name'], 
                    'column': column.name, 
                    'data': processed
                })
    tmpdict = {}
    for i in result:
        tmpdict[f'function: {i.name} name: {i.column}'] = i.data
    df = DataFrame(tmpdict)
    df.to_excel(f"data/{id}.xlsx")
    df.to_csv(f"data/{id}.xlsx")

    plt.figure(num=None, figsize=(math.ceil(math.sqrt(df.size)), math.ceil(math.sqrt(df.size)))*3, dpi=800, facecolor='w', edgecolor='k')
    i=1
    for i in df:
        plt.subplot(math.ceil(math.sqrt(df.size)),math.ceil(math.sqrt(df.size)),i)
        plt.plot(df['i'].values())
        plt.title(f'{str(i)}')
        i +=1
    plt.savefig(f'images/{id}.png')
    plt.clf()
    plt.close()
