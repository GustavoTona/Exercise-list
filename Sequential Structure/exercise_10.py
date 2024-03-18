# Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
C = float(input("Temperatura em Celsius: "))

F = (C * 1.8) + 32

print(format(F,'.0f'),'Fahrenheit')

