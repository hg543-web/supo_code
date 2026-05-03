import numpy as np
import math


def fxy(v):
    x, y = v[0], v[1]
    return (2-x)**2 + 100*(y-x**2)**2

def fdashxy(v):
    x, y = v[0], v[1]
    return np.array([(-2*(2-x))-(400*x*(y-(x**2))),200*(y-(x**2))])

def fdashdashxy(v):
    x, y = v[0], v[1]
    return np.array([[2 - 400*y + 1200*(x**2), -400*x],[-400*x,200]])

def partial(x0,y0,tol):
    v = np.array([x0,y0])
    v0 = np.array([x0,y0])
    
    while (np.linalg.norm(fdashxy(v))/np.linalg.norm(fdashxy(v0)))>tol:
        vnew = v - np.linalg.solve((fdashdashxy(v)),(fdashxy(v)))
        v = vnew
    return v

print(partial(1.1,1.1,10**-9))
