'''

Faça um programa que calcule o fatorial de um número inteiro fornecido pelo usuário. Ex.: 5!=5.4.3.2.1=120


'''

num = int(input('Digite o numero para o fatorial: '))

def factorial(n):
      # Verifica se o número é igual a zero
    if n == 0:
        return 1  # Retorna 1 se o número for zero, pois 0! é definido como 1
    result = 1  # Inicializa o resultado como 1
    # Loop para calcular o fatorial de n
    for i in range(1, n + 1):  # Itera de 1 até n (inclusive)
        result *= i  # Multiplica o resultado pelo valor atual do loop
    return result  # Retorna o resultado do fatorial

# Testando a função
print(factorial(num))  # Saída: 120