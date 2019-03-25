import numpy as np
import scipy as sc


## Basic functions
def mean(input):
    return np.mean(input)
def var(input):
    return np.var(input)
def amplitude(input,step):
    return input[step:] - input[:step]
def skew(input):
    return sc.stats.skew(input)
def kurtosis(input):
    return sc.stats.kurtosis(input)
def lam(input,lamb):
    return lamb(input)

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
