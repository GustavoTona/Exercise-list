'''

Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao usuário a valor do saque e depois informar quantas notas de cada valor serão fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor mínimo é de 10 reais e o máximo de 600 reais. 
O programa não deve se preocupar com a quantidade de notas existentes na máquina.
Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e quatro notas de 1.

'''

quantia = int(input('Qual o valor do saque?'))

notas_100 = (quantia // 100)
notas_50 = (quantia % 100) // 50
notas_10 = ((quantia % 100) % 50) // 10
notas_5 = (((quantia % 100) % 50) % 10) // 5
notas_1 = (((quantia % 100) % 50) % 10) % 5

print(f'Notas de 100 reais: {notas_100}')
print(f'Notas de 50 reais: {notas_50}')
print(f'Notas de 10 reais: {notas_10}')
print(f'Notas de 5 reais: {notas_5}')
print(f'Notas de 1 real: {notas_1}')


