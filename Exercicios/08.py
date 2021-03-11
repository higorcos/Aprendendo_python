salario = float(input('Qual o seu salário? R$:'))
aumento = 0.15
salarioFinal = (salario*aumento)+ salario

print('O salário de R${:.2f}, com o aumento de 15%, ficará {:.2f}'.format(salario,salarioFinal))