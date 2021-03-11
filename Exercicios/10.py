dias = int(input('Por quantos dia você alugou o carro? '))
km = float(input('Quantos km você pecorreu com o carro? '))
custoTotal = (km * 0.15) + (dias * 60) 
print('O total a se pagar é de R$:{}'.format(custoTotal))