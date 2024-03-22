'''
Faça um Programa que peça um número e informe se o número é inteiro ou decimal. 
Dica: utilize uma função de arredondamento.
'''

num = float(input())

#Round usado para arredondar o número digitado pelo usuário. Se o número arredondado for igual ao número original,
if num == round(num): 
    print('Esse número é inteiro')
else: 
    print('Esse número é decimal')