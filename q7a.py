import numpy as np
import math


def fx(x):
    return x**3 + x**2

def dydx(x):
    return 3*x**2 + 2*x

def ddydxx(x):
    return 6*x + 2

def single(x0, tol):
    x = x0
    while (dydx(x)/dydx(x0))>tol:
        y = x - ((ddydxx(x))**-1)*(dydx(x))
        x = y
    return x

print(single(-1,0.01))
print(single(1,0.01))

