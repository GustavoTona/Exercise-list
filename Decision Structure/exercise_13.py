'''
Faça um Programa que leia um número e exiba o dia correspondente da semana. 
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
'''

num = int(input('Dia da semana: '))

dia_semana = ['domingo','segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sabado']

indice = num - 1 #subtrai um numero para ajustar no array

dia = dia_semana[indice]

print(dia)


