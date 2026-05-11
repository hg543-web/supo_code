import numpy as np
from scipy import linalg

# Defining matrices
K = np.array([[2, -1], [-1, 3]])
M = np.array([[1, 0], [0, 2]])

# Solve the  eigenvalue problem: K*v = lambda*M*v (determinant = 0)
# D returns eigenvalues, V returns eigenvectors
D, V = linalg.eig(K, M)

# Sort
idx = D.argsort()
D = D[idx]
V = V[:, idx]

for n in range(len(D)):
    mode = V[:, n]
    
    # Normalize mode relative to the first element
    mode = mode / mode[0]
    
    # Get the eigenvalue (squared frequency)
    freq2 = D[n].real
    
    print(f"Mode {n+1} has squared frequency {freq2:g} and mode [{mode[0]:g}, {mode[1]:g}]")