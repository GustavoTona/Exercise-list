'''

Faça um programa que, dado um conjunto de N números, determine o menor valor, o maior valor e a soma dos valores.

'''

menor_numero = float('inf')  # Inicializa o menor número com infinito 
maior_numero = float('-inf')  # Inicializa o maior número com menos infinito
soma = 0 #Inicializa com zero

for i in range(3):
    numero = int(input(f"Digite o {i+1}º número: ")) 
    soma += numero  # Adiciona o número atual à soma total
    
    # Verifica se o número atual é menor
    if numero < menor_numero:
        menor_numero = numero  # Atualiza o menor número encontrado até agora
    
    # Verifica se o número atual é maior 
    if numero > maior_numero:
        maior_numero = numero  # Atualiza o maior número encontrado até agora

print("O menor número digitado foi:", menor_numero)
print("O maior número digitado foi:", maior_numero)
print("O total do número digitado foi:", soma)





