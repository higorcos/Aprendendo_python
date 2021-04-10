import numpy as arr
a = arr.array([[0,1,5,5,5],[0,5,5,5,5],[1,2,3,4,5]])
##print(a)
##print(a.ndim)## qual a dimenção 
##print(a.shape)## qual a configuração / linhas e colunas
##print(len(a)) 

b = arr.arange(0, 99, 1) ## Adiciona de forma automática ## paremetros (inicio, fim, passos) o número que vc coloca no "fim" não conta só o anterior a ele
##b = arr.arange(10, 20) ##Passo de 1 em 1 (10 a 20(20 -1 = 19))
##b = arr.arange(10) ## Passo automatica de um em 1 de 0 a 10(10-1 = 9)
##print(b)
linhas = int(2)
colunas = int(3)
c = arr.ones((linhas,colunas)) ## matrix bidimensional com 1
##c = arr.ones(5) ## matrix unidimensinal com 1
##print(c)
d = arr.zeros(9) # matix unidemensinal com 0
# print(d)

f = arr.random.rand(3)# gera matrix aleatória #parametro é o numero linha e colunas 
print(f)

