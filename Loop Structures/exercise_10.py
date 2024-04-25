'''
Faça um programa que imprima na tela apenas os números ímpares entre 1 e 50.
'''

contador_impares = 0  # Inicializa o contador de números ímpares

for num in range(1, 51):  # Loop de 1 a 50
    # Verifica se o número é ímpar
    if num % 2 != 0:
        print(num)  # Se for ímpar, imprime o número
        contador_impares += 1  # Incrementa o contador de números ímpares

# Imprime a quantidade de valores ímpares
print("A quantidade de números ímpares entre 1 e 50 é:", contador_impares)





