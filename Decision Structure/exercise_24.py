'''

Faça um Programa que leia 2 números e em seguida pergunte ao usuário qual operação ele deseja realizar. O resultado da operação deve ser acompanhado de uma frase que diga se o número é:
par ou ímpar;
positivo ou negativo;
inteiro ou decimal.

'''
num_1  = float(input('Digite um numero: '))
num_2 = float(input('Digite mais um numero: '))

operacao = (input('Qual operação você deseja fazer? somar, subtrair, multiplicar, divisão. '))

if operacao.lower() == "somar": 
    resultado = num_1 + num_2 
elif operacao.lower() == "subtrair": 
    resultado = num_1 - num_2 
elif operacao.lower() == "multiplicar": 
    resultado = num_1 * num_2 
elif operacao.lower() == "divisão": 
    resultado = num_1 / num_2 

print(f'O resultado da operação {operacao} é: {resultado}')

if  resultado == round(resultado): 
    print('Esse número é inteiro') 
else: 
    print('Esse número é decimal')

if resultado % 2 == 0: 
    print('Esse numero é par')
else: 
    print('Esse numero é impar')

if resultado > 0: 
    print('Esse numero é positivo')
else: 
    print('Esse numero é negativo')