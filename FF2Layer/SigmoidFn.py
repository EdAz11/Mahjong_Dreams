import math

def output(x):
    return 1/(1+math.exp(-x))

def derivative(x):
    return x*(1-x)