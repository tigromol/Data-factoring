import datetime

from flask import Blueprint, make_response, request, jsonify
from models import Column, Data
from utils.parse import parse
from utils.make_celery import celery
from werkzeug.utils import secure_filename
from Funcdicts.functions_base import funcdict
import constants as constants
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
        req_file.stream.seek(0)
        new_data.file.put(req_file, content_type='text/csv', filename=req_file.filename, encoding='utf-8')
        new_data.save()
        result = {
            'id': str(new_data.id),
            'data': lists_to_csv([{'name': column.name, 'data': column.data} for column in new_data.columns]),
            'type': constants.LINE_CHART
        }
        return jsonify(result), 200

def lists_to_csv(columns):
    result = []
    for column in columns:
        if not isinstance(column['data'], (list, dict)):
            column['data'] = [column['data']]
    max_length = max(*[len(column['data']) for column in columns])
    result.append(["X", *[column['name'] for column in columns]])
    result.extend(list(zip(list(range(max_length)), *[column['data'] for column in columns])))
    return result

@data.route('/<id>', methods=['GET'])
def preprocess(id):
    req_body = request.get_json()

    filter_columns = req_body['columns']
    single_functions = req_body['singleFunctions']
    cascade_functions = req_body['cascadeFunctions']

    data = Data.objects.get(id=id).columns
    data = [
        {
            'name': column.name, 
            'data': [num for num in column.data if isinstance(num, (int, float))]
        } for column in data if column.name in filter_columns
    ]

    result = []

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
        result.append(
            {
                'name': function['name'], 
                'data': lists_to_csv(temp_data),
                'type': return_type
            }
        )

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
        result.append(
            {
                'name': ', '.join(function_names),
                'data': lists_to_csv(processed_data),
                'type': return_type
            }
        )

    return jsonify(result), 200

@data.route('/<dataId>', methods=['PUT'])
def process(dataId):
    req = request.get_json()
    task = celery.send_task('tasks.add', args=(dataId, req['email'], req['singleFunctions'], req['cascadeFunctions'], req['columns']))
    return make_response(f"Ok", 200)
    


