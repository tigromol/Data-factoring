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

        data = Data(
            created = datetime.datetime.now(),
            columns = cols
        )
        data.file.put(req_file)
        data.save()
        return data.json(), 200

@data.route('/<id>', methods=['GET'])
def preprocess(id):
    result = []
    req_body = request.get_json()
    columns = req_body['columns']
    functions = req_body['functions']
    print(Data.objects.get(id=id).columns)
    data = Data.objects.get(id=id).columns
    data = [column for column in data if column.name in columns]
    for column in data:
        for function in functions:
            if isinstance(function,list):
                processed = list(column['data'])
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
                processed = func(inp=np.array(column['data']), **function['args'])
                result.append({
                    'name': function['name'], 
                    'column': column.name, 
                    'data': processed
                })
    return jsonify(result), 200


    


