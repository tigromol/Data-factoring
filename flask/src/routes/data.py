import datetime

from flask import Blueprint, make_response, request, jsonify
from models import Column, Data
from utils.parse import parse
from werkzeug.utils import secure_filename
from Funcdicts.functions_base import funcdict
import numpy as np

data = Blueprint('data', __name__)

@data.route('/', methods=['POST'])
def upload():
    if 'file' not in request.files:
        return make_response('No file sent', 400)

    req_file = request.files['file']

    if req_file.filename == '':
        return make_response('No file selected', 400)
        
    if req_file:
        filename = secure_filename(req_file.filename)
        parsed_file = parse(req_file, 500)

        cols = []
        for k, v in parsed_file.items():
            cols.append(Column(name = k, data = v))

        new_data = Data(
            created = datetime.datetime.now(),
            columns = cols
        )
        new_data.file.put(req_file)
        new_data.save()

        result = {
            'id': str(new_data.id),
            'data': lists_to_csv(new_data.columns)
        }
        return jsonify(result), 200

def lists_to_csv(columns):
    result = []
    max_length = max(*[len(column.data) for column in columns])
    result.append(["X", *[column.name for column in columns]])
    result.extend(list(zip(list(range(max_length)), *[column.data for column in columns])))
    return result

@data.route('/<id>', methods=['GET'])
def preprocess(id):
    result = []
    req_body = request.get_json()
    columns = req_body['columns']
    functions = req_body['functions']
    data = Data.objects.get(id=id).columns
    print(f"data before process: {[column.name for column in data]}")
    data = [column for column in data if column.name in columns]

    print(f"data after process: {[column.name for column in data]}")
    print(f"columns: {columns}")
    print(f"functions: {functions}")


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
    return jsonify(result), 200
@data.route('/<id>', methods=['PUT'])
def process():
    result = []
    req_body = request.get_json()
    columns = req_body['columns']
    functions = req_body['functions']
    data = Data.objects.get(id=id).columns
    print(f"data before process: {[column.name for column in data]}")
    data = [column for column in data if column.name in columns]

    print(f"data after process: {[column.name for column in data]}")
    print(f"columns: {columns}")
    print(f"functions: {functions}")


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
    return jsonify(result), 200

    


