import numpy as np
def func(x):
    return 3*x**2

def one_sided_diff(x,h):
    return (func(x+h)-func(x))/h

def symmetric_diff(x,h):
    return (func(x+h)-func(x-h))/(2*h)

def test(x,h):
    exact = 6*x
    one_sided_error = (one_sided_diff(x,h) - exact)/exact
    symmetric_error = (symmetric_diff(x,h) - exact)/exact
    print ("percentage error of one sided difference: " + str(f"{100*one_sided_error:.3g}") +"%" + "\n" + "Percentage error of symmetrical difference: " + str(f"{100*symmetric_error:.3g}")+"%")

test(3,0.1)