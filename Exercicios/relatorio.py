print('Oi, hoje o Python vai contar uma fábula para você...') #avisa que vai contar uma história
print('')# cria um linha sem caracteres para organizar o código

#Nessa parte do código o computador vai fazer algumas perguntas para o usuário
#as respostas dessas perguntas serão usadas para completar a história.

name = str(input('Qual o sua sugestão de nome para o personagem principal ? '))
age = int(input('E a idade dele(a) ? '))
fruit = str(input('Fale um nome de uma fruta ? '))

#Nessa parte o computador vai printar o texto no terminal e vai completar com as respostas do usuário.

print('')
print('Uma raposa(o) faminta(o) chamada(o) {} que tinha {} anos de idade, ao ver uma {}'.format(name,age,fruit)) #as variáveis serão printadas no terminal nas ordem  (name,age,fruit)
print('quis pegá-la(o) mas não conseguiu. Então, afastou-se da fruta, dizendo: “Não queria mesmo”.')
print('') #linha em branco para organização
print('Moral da História: ')
print('Assim como a/o {}, algumas pessoas não conseguem alcançar'.format(name)) # a variável é colocada dentro dos {}
print('seus objetivo e acabam criando desculpas para o fracasso.')
print('') #linha em branco para organização