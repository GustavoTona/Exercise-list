'''

Altere o programa de cálculo do fatorial, permitindo ao usuário calcular o fatorial 
várias vezes e limitando o fatorial a números inteiros positivos e menores que 16.

'''

def factorial(n):
    """Calcula o fatorial de um número n."""
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

while True:
    # Solicita ao usuário um número para calcular o fatorial
    num = input('Digite o número para o fatorial (ou "sair" para encerrar): ')
    
    # Permite ao usuário sair do loop
    if num.lower() == 'sair':
        print("Programa encerrado.")
        break
    
    try:
        num = int(num)
    except ValueError:
        print("Por favor, digite um número inteiro.")
        continue

    # Verifica se o número está dentro do intervalo permitido
    if num < 0 or num > 15:
        print("Digite um número inteiro positivo menor que 16.")
        continue
    
    # Calcula e exibe o fatorial do número
    print(f"O fatorial de {num} é {factorial(num)}")

