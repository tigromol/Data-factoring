import numpy as np
import scipy as sc


## Basic vector functions (end functions)
def mean(**kwargs):
    return np.mean(kwargs['inp'])

def var(**kwargs):
    return np.var(kwargs['inp'])

def skew(**kwargs):
    return sc.stats.skew(kwargs['inp'])

def kurtosis(**kwargs):
    return sc.stats.kurtosis(kwargs['inp'])

# Basic vector functions (vector output)
def amplitude(**kwargs):
    return kwargs['inp'][kwargs['step']:] - kwargs['inp'][:kwargs['step']]

def lam(**kwargs):
    return kwargs['lamb'](inp = kwargs['inp'])

#matrix functions
def matrixlam(**kwargs):
    data = []
    for i in kwargs['input']:
        data.append(lam(inp= i,lamb = kwargs['lamb']))
    return data

def matrixfunc(**kwargs):
    data = []
    for i in kwargs['inp']:
        data.append(kwargs['func'](i))
    return data

def matrixize(**kwargs):
    data = [[0]]
    for i in range(kwargs['step']):
        data.append(amplitude(inp = kwargs['inp'],step = i))
    return data[1:]

# Histo function
def histo(**kwargs):
    return np.histogram(kwargs['inp'],kwargs['bins'],**kwargs)
## Lambda functions
def mult(**kwargs):
    return kwargs['inp'] * kwargs['mult']
def div(**kwargs):
    return kwargs['inp'] / kwargs['div']
def add(**kwargs):
    return kwargs['inp'] + kwargs['add']
def subs(**kwargs):
    return kwargs['inp'] - kwargs['subs']
def pwr(**kwargs):
    return kwargs['inp']**kwargs['pwr']

funcdict = {
    'mean':mean,
    'var':var,
    'skew':skew,
    'kurtosis':kurtosis,
    'amplitude':amplitude,
    'lam':lam,
    'matrixlam':matrixlam,
    'matrixfunc':matrixfunc,
    'matrixize':matrixize,
    'histo':histo,
    'lambda':{
        'mult':mult,
        'div':div,
        'add':add,
        'subs':subs,
        'pwr':pwr
    }
    
}