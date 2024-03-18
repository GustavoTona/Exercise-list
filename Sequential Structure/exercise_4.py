# Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota_1, nota_2, nota_3, nota_4 = map(int, input().split())

media = (nota_1 + nota_2 + nota_3 + nota_4)/ 4 

print('A média é:', media)