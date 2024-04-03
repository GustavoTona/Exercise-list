'''

Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

Altere o programa anterior para que ele aceite apenas números entre 0 e 1000.

'''

menor_numero = 1001  # Inicializa o menor número com um valor maior que 1000
maior_numero = -1  # Inicializa o maior número com um valor menor que 0
soma = 0

for i in range(3):
    numero = int(input(f"Digite o {i+1}º número (entre 0 e 1000): "))
    
    # Verifica se o número está dentro do intervalo desejado
    while numero < 0 or numero > 1000:
        print("Número inválido! Por favor, insira um número entre 0 e 1000.")
        numero = int(input(f"Digite o {i+1}º número (entre 0 e 1000): "))
    
    soma += numero
    if numero < menor_numero:
        menor_numero = numero
    if numero > maior_numero:
        maior_numero = numero

    
print("O menor número digitado foi:", menor_numero)
print("O maior número digitado foi:", maior_numero)
print("O total do número digitado foi:", soma)





