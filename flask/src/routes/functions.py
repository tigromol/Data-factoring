from flask import Blueprint

functions = Blueprint('functions', __name__)

@functions.route('/diff', methods='POST')
def execute_diff(func,**kwargs):
    return func(**kwargs)

@functions.route('/uni',methods='POST')
def execute_uni(*args,**kwargs):
    for i in args:
        tmp = i(input=kwargs['input'])
        kwargs['input'] = tmp
    return tmp
