import datetime

from flask import Blueprint, make_response, request
from models import Column, Data
from utils.parse import parse
from werkzeug.utils import secure_filename
from Funcdicts.functions_base import funcdict

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
    json = request.get_json()
    columns = json['columns']
    functions = json['functions']
    data = list(filter(lambda x: x.name in columns,Data.objects(id=id).columns))
    for i in data:
        for j in functions:
            if isinstance(j,list):
                for k in j:
                    i['data'] = funcdict[k['function']['name']]['func'](inp = np.array(i['data']),**k['args'])
            else :
                i['data'] = funcdict[k['function']['name']]['func'](inp = np.array(i['data']),**j['args'])
    return data, 200


    


