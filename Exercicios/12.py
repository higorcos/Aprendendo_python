#%%no 

import numpy as np
import matplotlib.pyplot as  plt

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
# plot seno e cosseno
plt.style.use('seaborn') #estilo especifico para a tabela 
plt.figure(figsize=(9,5))#tamanho da imagem 
plt.title('Seno e cosseno em duas voltas no sentido anti-horário') #titulo para a  tabela 
plt.plot(graus, y2, label='Seno') #Vai aplicar o valor de seno na tabela 
plt.plot(graus, y1, label='Cosseno') # vai  aplicar o valor de cosseno na tabela
plt.legend() #Vai ativar o label "legenda"

""" 
   Radianos        Graus                        seno                cosseno                  
-6.28318531     -36000000016,25 (-360)      -0.9589156775704306     -0.2836912464452188       
-3.14159265     -17999999979,48 (-180)       0.8011525126425406     -0.5984602338389275
0.              0               (0)          0                       1
3.14159265      17999999979,48  (180)       -0.8011525126425406     -0.5984602338389275       
6.28318531      36000000016,25  (360)        0.9589156775704306     -0.2836912464452188
 """
# %%
