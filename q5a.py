import numpy as np
import matplotlib.pyplot as pyplot
# f(x) = sin(x) + cos(10x)/5 array generation
fx = []
for i in range(51):
    fx.append(np.sin(i*np.pi/25) + ((np.cos(10*i*np.pi/25)/5)))


# running average function
# Had previously done 'for i in array,' but this gave the small float values from the array, leading to repeated small datum
def running_average(array):
    avg = []
    for i in range(2, len(array)):
        if i <= 1:
            pass
        avg.append((array[i] + array[i-1] + array[i-2])/3)
        #print(str(f"{avg:.4g}"))
    return avg

running_average(fx)
# creating x-axis
xn_axis = range(2,51)
x_axis = []
for i in xn_axis:
    x_axis.append(i*np.pi/25)



pyplot.plot(x_axis, running_average(fx))
fx=fx[1:50]
pyplot.plot(x_axis, fx)
pyplot.show()