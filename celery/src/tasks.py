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
def process(id, email, single_functions, cascade_functions, filter_columns):
    connect('datafactoring', host='mongo', port=27017, username='admin', password='admin')
    plt.subplots_adjust(wspace=2.2,hspace=2.2)
    result = {}
    file = Data.objects().get(id=id).file.get()
    data = parse(file)

    data = [
        {
            'name': column, 
            'data': [num for num in data if isinstance(num, (int, float))]
        } for column, data in data.items() if column in filter_columns
    ]

    result = {}

    for function in single_functions:
        temp_data = []
        func = funcdict[function['name']]['func']
        return_type = funcdict[function['name']]['type']
        for column in data:
            processed = func(inp=np.array(column['data']), **function['args'])
            temp_data.append({
                'name': column['name'],
                'data': processed
            })

        for column in temp_data:
            result[f"column: {column['name']} function: {function['name']}"] = column['data']

    for functions in cascade_functions:
        function_names = []
        temp_processed = {}
        return_type = -1
        for function in functions:
            func = funcdict[function['name']]['func']
            return_type = funcdict[function['name']]['type']
            function_names.append(function['name'])
            for column in data:
                processed = func(inp=np.array(column['data']), **function['args'])
                temp_processed[column['name']] = processed
        processed_data = [{'name': k, 'data': v} for k, v in temp_processed.items()]
        for column in processed_data:
            result[f"column: {column['name']} functions: {', '.join(function_names)}"] = column['data']
    
    df = DataFrame.from_dict(result)
    df.to_excel(f"data/{id}.xlsx")
    df.to_csv(f"data/{id}.csv")
    plt.figure(num=None, figsize=(math.ceil(math.sqrt(df.shape[1])), math.ceil(math.sqrt(df.shape[1]))), dpi=800, facecolor='w', edgecolor='k')
    j = 1
    for i in df:
        plt.subplot(math.ceil(math.sqrt(df.shape[1])), math.ceil(math.sqrt(df.shape[1])), j)
        plt.plot(list(df[i].values))
        plt.title(f'{str(i)}')
        j += 1
    plt.savefig(f'images/{id}.png')
    plt.clf()
    plt.close()
