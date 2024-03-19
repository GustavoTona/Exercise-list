'''
Faça um programa que pergunte o preço de três produtos e informe qual produto você deve comprar, 
sabendo que a decisão é sempre pelo mais barato.
'''

produto_1 = int(input())
produto_2 = int(input())
produto_3 = int(input())

menor = min(produto_1, produto_2, produto_3)

if menor == produto_1:
    print('Compre o primeiro produto')
elif menor == produto_2:
    print('Compre o segundo produto')
else:
    print('Compre o terceiro produto')

