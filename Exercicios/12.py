import numpy as np
from matplotlib.pyplot import subplots

a = np.linspace(-2*np.pi,2*np.pi, 5)
print('Radiano',a)
#conversão
graus = (a* 180/np.pi) #vai transformar o radianos em graus
print('Graus',graus) # será aproximado 
# cosseno
y1 = np.cos(graus)
# seno
y2 = np.sin(graus)
print('Seno',y2)
print('Cosseno',y1)
print('')
fig, ax = subplots(1,2)
# plot seno
ax[0].plot(graus, y2)
ax[0].set_title("Funçao Seno")
# plot cosseno
ax[1].plot(graus, y1)
ax[1].set_title("Funçao Cosseno")




