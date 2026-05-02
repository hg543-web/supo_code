import numpy as np
def func(x):
    return (x**2)*(np.sin(x**2))

def complex_step_method(x,h):
    return ((func(x+(1j*h))-func(x))/h).imag

def symmetric_diff(x,h):
    return (func(x+h)-func(x-h))/(2*h)

def test(x,h):
    exact = (2*x*np.sin(x**2))+(2*x*(x**2)*np.cos(x**2))
    one_sided_error = (complex_step_method(x,h) - exact)/exact
    symmetric_error = (symmetric_diff(x,h) - exact)/exact
    print ("percentage error of complex step method: " + str(f"{100*one_sided_error:.3g}") +"%" + "\n" + "Percentage error of symmetrical difference: " + str(f"{100*symmetric_error:.3g}")+"%")


for x in [10,100,1000,10000]:
    print("when x = " + str(x))
    for h in [10**-9, 10**-12, 10**-15]:
        print("For h = " + str(h))
        test(x,h)