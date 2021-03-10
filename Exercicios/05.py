moedaBR = float(input('Qual o valor total que você tem na sua conta agora ? R$:'))
precoUS = 5.65 #preço atual 
moedaUS = float(moedaBR / precoUS)
print('Convertendo {:.2f} para dólar americano você teria {:.2f}'.format(moedaBR, moedaUS))