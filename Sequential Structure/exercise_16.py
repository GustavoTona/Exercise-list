"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados
 da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 3 metros 
 quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. Informe ao 
 usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""
import math

metros = float(input("Qual o metro quadrado da area? "))

litros = metros / 3 # divir os metros por cada litro pinta 3 metros


lata = litros / 18 # divir o litro para quanto vem em cada lata
lata = math.ceil(lata) #Arredondar os valores para cima! 

preco = lata * 80.00  # quantas para ter o preço total 


print("Para pintar a parede precisa de: ",round(litros ,2), "Litros")
print("Será necessário:", round(lata, 2), "latas de tintas")
print("Total:",round(preco, 2),"R$")

