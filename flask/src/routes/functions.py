from flask import Blueprint
from functions_base import funcdict
import numpy as np

functions = Blueprint('functions', __name__)

@functions.route('/diff', methods='POST')
def execute_diff(func,**kwargs):
    return func(**kwargs)

@functions.route('/uni',methods='POST')
def execute_uni(*args,**kwargs):
    for i in args:
        kwargs['inp'] = i(**kwargs)
    return kwargs['inp']


test = execute_diff(funcdict['amplitude'],inp = np.array([1,2,3,4,5,6]),step = 1)
print(test)


test = execute_uni(funcdict['amplitude'],funcdict['lambda']['pwr'],funcdict['lambda']['add'],inp=np.array([1,2,3,4,5,6]),step = 1,pwr=2,add=2)
print(test)
 