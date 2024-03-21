'''
Faça um Programa que peça um número inteiro e determine se ele é par ou impar. Dica: utilize o operador módulo (resto da divisão).

'''

num = int(input())

resultado = num % 2 

if resultado == 0: 
    print('Esse numero é par')
else: 
    print('Esse numero é impar')