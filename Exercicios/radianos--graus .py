# conversão
import numpy as np

x = 6.28318531

Graus = (x * 180/np.pi)
print(Graus)
y1 = np.sin(Graus)
y2 = np.cos(Graus)
print(y1,y2)