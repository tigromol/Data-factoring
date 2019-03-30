import numpy as np
import scipy as sc



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
    'mean':{'func': mean,
            'args': {'inp':'input vector'},
            'display': 'Mean value'},
    'var':{'func':var,
            'args': {'inp':'input vector'},
            'display': 'Variance value'},
    'skew':{'func':skew,
            'args': {'inp':'input vector'},
            'display': 'Skewness value'},
    'kurtosis':{'func':kurtosis,
            'args': {'inp':'input vector'},
            'display': 'Kurtosis value'},
    'amplitude':{'func':amplitude,
            'args': {'inp':'input vector','step':'Step interval for amplitude calculation'},
            'display': 'Amplitudes of lit'},
    'matrixlam':{'func':matrixlam,
            'args': {'inp':'input vector','lab':'lambda function from dict (that which evaluate in list'},
            'display': 'Evaluate each column in matrix with lambda function'},
    'matrixfunc':{'func':matrixfunc,
            'args': {'inp':'input vector','func':'Function to apply to columns in matrix'},
            'display': 'Compute each column in matrix with function'},
    'matrixize':{'func':matrixize,
            'args': {'inp':'input vector',
            'step':'numbers of iterations to form a matrix (e.g step=3 evalute in len(inp) x 3 matrix',
            'func':'function to apply'},
            'display': 'Compute matrix for diff steps of function'},
    'histo':{'func':histo,
            'args': {'inp':'input vector','bins':'number of bins'},
            'display': 'Compute distributions'},
    'mult':{'func':mult,
            'args': {'inp':'input vector','mult':'lambda value'},
            'display': 'Lambda function multiply'},
    'div':{'func':div,
            'args': {'inp':'input vector','div':'lambda value'},
            'display': 'Lambda function divide'},
    'add':{'func':add,
            'args': {'inp':'input vector','add':'lambda value'},
            'display': 'Lambda function addition'},
    'subs':{'func':subs,
            'args': {'inp':'input vector','subs':'lambda value'},
            'display': 'Lambda function substract'},
    'pwr':{'func':pwr,
            'args': {'inp':'input vector','pwr':'lambda value'},
            'display': 'Lambda function power'}

    
}
