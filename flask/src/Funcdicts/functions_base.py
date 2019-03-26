import numpy as np
import scipy as sc


## Basic vector functions (end functions)
def mean(input):
    return np.mean(input)

def var(input):
    return np.var(input)

def skew(input):
    return sc.stats.skew(input)

def kurtosis(input):
    return sc.stats.kurtosis(input)

# Basic vector functions (vector output)
def amplitude(input,step):
    return input[step:] - input[:step]

def lam(input,lamb):
    return lamb(input)

#matrix functions
def matrixlam(input,lamb):
    data = []
    for i in input:
        data.append(lam(i,lamb))
    return data

def matrixfunc(input,func):
    data = []
    for i in input:
        data.append(func(i))
    return data

def matrixize(input,step):
    data = [[0]]
    for i in range(step):
        data.append(amplitude(input,step))
    return data[1:]

# Histo function
def histo(arg,bins=10,dens=False):
    return np.histogram(arg,bins,density=dens)
## Lambda functions
def mult(arg):
    return lambda x: x*arg
def div(arg):
    return lambda x: x/arg
def add(arg):
    return lambda x: x+arg
def subs(arg):
    return lambda x: x-arg
def pwr(arg):
    return lambda x: x**arg

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
    
}