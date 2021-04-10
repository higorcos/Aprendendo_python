import numpy as np
from matplotlib.pyplot import subplots

a = np.linspace(-2*np.pi,2*np.pi, 5)
print(a)
# cosseno
y1 = np.cos(a)
# seno
y2 = np.sin(a)
fig, ax = subplots(1,2)
# plot seno
ax[0].plot(a, y2)
ax[0].set_title("Funçao Seno")
# plot cosseno
ax[1].plot(a, y1)
ax[1].set_title("Funçao Cosseno")




