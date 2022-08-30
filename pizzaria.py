total = 0
produto = 0
codigo = 0
tamanho = 0

cliente = input('Digite seu nome: ')  # Indentificador cliente
print('Bem vindo a fortaleza da pizza \nSr(a) ',cliente)

print('\n', '-' * 27, 'CARDÁPIO', '-' * 27)
print('| CÓDIGO  |   DESCRIÇÃO   |   PIZZA MÉDIA   |   PIZZA GRANDE   |')
print('|   21    |   Napolitana  |       R$20,00   |       R$ 26,00   |')
print('|   22    |   Margherita  |       R$20,00   |       R$ 26,00   |')
print('|   23    |   Calabresa   |       R$25,00   |       R$ 32,00   |')
print('|   24    |   Toscana     |       R$30,00   |       R$ 39,00   |')
print('|   25    |   Portuguesa  |       R$30,00   |       R$ 39,00   |')
print('-' * 64)

              #Produto 01
while produto == 0:

  codigo = input('Entre com o codigo do produto: ')
  tamanho = input('Qual o tamanho da pizza? ')
  if codigo == '21' and tamanho == 'm':
    total = total + 20
    print ('Você pediu uma pizza Média de Napolitano?')
  elif codigo == '21' and tamanho == 'g':
    total = total + 26
    print ('Você pediu uma pizza Grande de Napolitano?')

            #Produto 02
  elif codigo == '22' and tamanho == 'm':
    total = total + 20
    print ('Você pediu uma pizza Média de Margherita?')
  elif codigo == '22' and tamanho == 'g':
    total = total + 26
    print ('Você pediu uma pizza Grande de Margherita?')

              #Produto 03
  elif codigo == '23' and tamanho == 'm':
    total = total + 25
    print ('Você pediu uma pizza Média de Calabresa?')
  elif codigo == '23' and tamanho == 'g':
    total = total + 32
    print ('Você pediu uma pizza Grande de Calabresa?')

              #Produto 04
  elif codigo == '24' and tamanho == 'm':
    total = total + 30
    print ('Você pediu uma pizza Média de Toscana?')
  elif codigo == '24' and tamanho == 'g':
    total = total + 39
    print ('Você pediu uma pizza Grande de Toscana?')

              #Produto 05
  elif codigo == '25' and tamanho == 'm':
    total = total + 30
    print ('Você pediu uma pizza Média de Portuguesa?')
  elif codigo == '25' and tamanho == 'g':
    total = total + 39
    print ('Você pediu uma pizza Grande de Portuguesa?')
  else:
    print('Opção Inválda')
    continue
  resposta = input('Deseja pedir mais alguma coisa? \n1 - SIM\n0 - Não\n>>')
  if resposta == '1':
    continue
  else:

    print('O total a ser pago é: {:.2f}'.format(total))
    break

