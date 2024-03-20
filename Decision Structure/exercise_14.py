'''
Faça um programa que lê as duas notas parciais obtidas por um aluno numa disciplina ao longo de um semestre, e calcule a sua média.
 A atribuição de conceitos obedece à tabela abaixo:
'''

nota_1, nota_2 = map(float, input().split())

media = (nota_1 + nota_2) / 2 

if media < 4: 
  print('Você tirou um E')

elif media < 6:
  print('Você tirou um D')

elif media < 7.5:
  print('Você tirou um C')

elif media < 9:
  print('Você tirou um B')

else: 
  print('Você tirou um A')