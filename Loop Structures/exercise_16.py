'''

A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o nésimo termo.

'''

n = int(input('Digite um valor: '))  # Número de termos que você quer na série

# Inicializa os dois primeiros termos

if n < 500: 
    a, b = 0, 1

    for i in range(n):
        print(a, end=' ')
        a, b = b, a + b
else:
    print('O valor deve ser menor que 500')