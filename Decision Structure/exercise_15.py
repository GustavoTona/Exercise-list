'''
Faça um Programa que peça os 3 lados de um triângulo. 
O programa deverá informar se os valores podem ser um triângulo.
 Indique, caso os lados formem um triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
Três lados formam um triângulo quando a soma de quaisquer dois lados for maior que o terceiro;
Triângulo Equilátero: três lados iguais;
Triângulo Isósceles: quaisquer dois lados iguais;
Triângulo Escaleno: três lados diferentes;
'''

lado_1, lado_2, lado_3 = map(float, input().split())

if lado_1 + lado_2 > lado_3 and lado_2 + lado_3 > lado_1 and lado_1 + lado_3 > lado_2:
  if lado_1 == lado_2 == lado_3:
    print('É um triangulo Equilatero.')
  elif lado_1 != lado_2 != lado_3:
    print('É um triangulo Escaleno')
  else:
      print('É um triangulo Isoceles')
else:
  print('Os dados fornecidos não formam um triangulo')