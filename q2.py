import numpy as np


def func(x,y):
    z = x + y
    eigenvalues_ascending = np.linalg.eigvalsh(z)
    return eigenvalues_ascending

A = np.array([[1,1],[3,1]])
B = np.array([[2,-1],[-3,0]])

print(func(A,B))
assert func(A,B)[0] == 1
assert func(A,B)[1] == 3