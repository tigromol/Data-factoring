import numpy as np
import scipy as sc
import constants as constants


## Basic vector functions (end functions)

def mean(**kwargs):
    '''
    {'inp' : 'input vector'}
    '''
    return np.mean(kwargs['inp'])

def var(**kwargs):
    '''
    {'inp' : 'input vector'}
    '''
    return np.var(kwargs['inp'])

def skew(**kwargs):
    '''
    {'inp' : 'input vector'}
    '''
    return sc.stats.skew(kwargs['inp'])

def kurtosis(**kwargs):
    '''
    {'inp' : 'input vector'}
    '''
    return sc.stats.kurtosis(kwargs['inp'])

# Basic vector functions (vector output)

def amplitude(**kwargs):
    '''
    {'inp' : 'input vector','step' : 'step interval'}
    '''
    return (kwargs['inp'][kwargs['step']:] - kwargs['inp'][:-kwargs['step']]).tolist()



#matrix functions

def matrixlam(**kwargs):
    '''
   {'inp' : 'input vector','lam' : 'lambda function from dict'}
   '''
    data = []
    for i in kwargs['inp']:
        data.append(funcdict[kwargs['func']]['func'](**kwargs))
    return data

def matrixfunc(**kwargs):
    '''
    {'inp' : 'input vector','func' : 'function to implement to matrix'}
    '''
    data = []
    for i in kwargs['inp']:
        data.append(kwargs['func'](i))
    return data

def matrixize(**kwargs):
    '''
    {'inp' : 'input vector','step' : 'range for matrixation (e.g step = 3 resolves in matrix len(inp) X 3)'}
    '''
    data = [[0]]
    for i in range(int(kwargs['step'])):
        data.append(kwargs['func'](inp = kwargs['inp'],step = i))
    return data[1:]

# Histo function
def histo(**kwargs):
    '''
    { 'inp' : 'input vector','bins' : 'number of bins'}
    '''
    return np.histogram(kwargs['inp'],kwargs['bins'])#,**kwargs)
## Lambda functions
def mult(**kwargs):
    '''
    {'inp' : 'input vector','mult' : 'lambda value'}
    '''
    return kwargs['inp'] * kwargs['mult']
def div(**kwargs):
    '''
    {'inp' : 'input vector','div' : 'lambda value'}
    '''
    return kwargs['inp'] / kwargs['div']
def add(**kwargs):
    '''
    {'inp' : 'input vector','add' : 'lambda value'}
    '''
    return kwargs['inp'] + kwargs['add']
def subs(**kwargs):
    '''
    {'inp' : 'input vector','subs' : 'lambda value'}
    '''
    return kwargs['inp'] - kwargs['subs']
def pwr(**kwargs):
    '''
    {'inp' : 'input vector','pwr' : 'lambda value'}
    '''
    return kwargs['inp']**kwargs['pwr']

funcdict = {
    'mean': {
        'func': mean,
        'args': [],
        'description': '',
        'display': 'Mean value',
        'type': constants.NUMBER
    },
    'var': {
        'func': var,
        'args': [],
        'description': '',
        'display': 'Variance value',
        'type': constants.NUMBER
    },
    'skew': {
        'func': skew,
        'args': [],
        'description': '',
        'display': 'Skewness value',
        'type': constants.NUMBER
    },
    'kurtosis': {
        'func':kurtosis,
        'args': [],
        'description': '',
        'display': 'Kurtosis value',
        'type': constants.NUMBER
    },
    'amplitude': {
        'func':amplitude,
        'args': [
            {
                'name': 'step',
                'display': 'step',
                'description': 'Step interval for amplitude calculation'
            }
        ],
        'description': '',
        'display': 'Amplitudes of lit',
        'type': constants.LINE_CHART
    },
    # 'matrixlam': {
    #     'func':matrixlam,
    #     'args': [
    #         {
    #             'name': 'lab',
    #             'description':'lambda function from dict (that which evaluate in list',
    #             'display': 'lab'
    #         }
    #     ],
    #     'description': '',
    #     'display': 'Evaluate each column in matrix with lambda function'
    # },
    # 'matrixfunc': {
    #     'func': matrixfunc,
    #     'args': [
    #         {
    #             'name': 'func',
    #             'display': 'func',
    #             'description' :'Function to apply to columns in matrix'
    #         }
    #     ],
    #     'display': 'Compute each column in matrix with function',
    #     'description': ''
    # },
    # 'matrixize': {
    #     'func':matrixize,
    #     'args': [
    #         {
    #             'name': 'step',
    #             'description':'numbers of iterations to form a matrix (e.g step=3 evalute in len(inp) x 3 matrix',
    #             'display': 'step'
    #         },
    #         {
    #             'name': 'func',
    #             'description':'function to apply',
    #             'display': 'func'
    #         }
    #     ],
    #     'description': 'Compute matrix for diff steps of function',
    #     'display': 'matrixize'
    # },
    'histo': {
        'func': histo,
        'args': [
            {
                'name': 'bins',
                'display': 'bins',
                'description':'number of bins'
            },
        ],
        'description': 'Compute distributions',
        'display': 'histogram',
        'type': constants.HISTOGRAM
    },
    # 'mult':{
    #     'func': mult,
    #     'args': [
    #         {
    #             'name': 'mult',
    #             'display': 'mult',
    #             'description': 'lambda value'
    #         }
    #     ],
    #     'description': 'Lambda function multiply',
    #     'display': 'multiply'
    # },
    # 'div':{
    #     'func': div,
    #     'args': [
    #         {
    #             'name': 'div',
    #             'display': 'div',
    #             'description':'lambda value'
    #         }
    #     ],
    #     'description': 'Lambda function divide',
    #     'display': 'divide'
    # },
    # 'add':{
    #     'func': add,
    #     'args': [
    #         {
    #             'name': 'add',
    #             'display': 'add',
    #             'description':'lambda value'
    #         }
    #     ],
    #     'description': 'Lambda function addition',
    #     'display': 'addition'
    # },
    # 'subs':{
    #     'func': subs,
    #     'args': [
    #         {
    #             'name': 'subs',
    #             'display': 'subs',
    #             'description':'lambda value'
    #         }
    #     ],
    #     'description': 'Lambda function substraction',
    #     'display': 'substraction'
    # },
    # 'pwr':{
    #     'func': pwr,
    #     'args': [
    #         {
    #             'name': 'pwr',
    #             'display': 'pwr',
    #             'description':'lambda value'
    #         }
    #     ],
    #     'description': 'Lambda function power',
    #     'display': 'power'
    # },

    
}
