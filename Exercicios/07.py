preco = float(input('Informe o valor do produto: R$:'))
desconto = preco * 5 /100 #com 5% de desconto
precoComDesconto = preco - desconto
print('O produto que custava {} com o desconto de 5%, o produto sairá por {:.2f}'.format(preco, precoComDesconto))