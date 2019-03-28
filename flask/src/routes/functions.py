from flask import Blueprint , jsonify , request
from Funcdicts.functions_base import funcdict



functions = Blueprint('functions', __name__)
@functions.route('/', methods=['GET'])
def getfunctions():
    result = []
    for key, value in funcdict.items():
        result.append({'name':key,'display':value['display'],'args':value['args']})
    return jsonify(result), 200



