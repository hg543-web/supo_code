import numpy as np
import matplotlib.pyplot as pyplot

Existing = pyplot.imread("southwing.jpeg")

G = np.array([[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])

Edged = np.zeros(Existing.shape)
for i in range (Edged.shape[0]-2):
    for j in range (Edged.shape[1]-2):
        intermediate_sum = 0
        for x in range(3):
            for y in range(3):
                intermediate_sum += G[x,y]*Existing[i-1+x,j-1+y]
        Edged[i,j] = intermediate_sum
Edged = (Edged - Edged.min())/(Edged.max() - Edged.min())
pyplot.imshow(Edged, cmap='gray')
pyplot.show()