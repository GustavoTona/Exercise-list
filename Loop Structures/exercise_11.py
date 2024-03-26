'''
Altere o programa anterior para mostrar no final a soma dos números.
'''


a = int(input('Número A: '))
b = int(input('Número B: '))

soma = 0  # Inicializa a variável de soma

for num in range(a, b + 1):
    soma += num  # Adiciona o número atual à soma

# Imprime a soma dos números
print("A soma dos números no intervalo é:", soma)





