"""
Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área
a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a
tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam
R$ 25,00.

Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
comprar apenas latas de 18 litros;
comprar apenas galões de 3,6 litros;
misturar latas e galões, de forma que o desperdício de tinta seja menor. 
Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias.
"""
import math

# Tamanho da área a ser pintada em metros quadrados
area = float(input("Digite o tamanho da área a ser pintada em metros quadrados: "))

# Calcula a quantidade total de litros necessários, considerando 10% de folga
litros_necessarios = area / 6 * 1.1

# Calcula a quantidade mínima de latas de 18 litros e galões de 3,6 litros necessários
latas_18 = math.ceil(litros_necessarios / 18)
galoes_36 = math.ceil(litros_necessarios / 3.6)

# Preço para comprar apenas latas de 18 litros
preco_latas_18 = latas_18 * 80.00

# Preço para comprar apenas galões de 3,6 litros
preco_galoes_36 = galoes_36 * 25.00

# Misturar latas e galões para minimizar o desperdício de tinta
latas_mistura = math.floor(litros_necessarios / 18)
litros_restantes = litros_necessarios - latas_mistura * 18
galoes_mistura = math.ceil(litros_restantes / 3.6)
preco_mistura = latas_mistura * 80.00 + galoes_mistura * 25.00

# Exibe os resultados
print("\nQuantidade de tinta necessária:")
print(f"Latas de 18 litros: {latas_18}")
print(f"Galões de 3,6 litros: {galoes_36}")

print("\nPreços:")
print(f"Preço apenas com latas de 18 litros: R${preco_latas_18:.2f}")
print(f"Preço apenas com galões de 3,6 litros: R${preco_galoes_36:.2f}")
print(f"Preço misturando latas e galões: R${preco_mistura:.2f}")

