'''

A série de Fibonacci é formada pela seqüência 1,1,2,3,5,8,13,21,34,55,... 
Faça um programa capaz de gerar a série até o nésimo termo.

'''

n = 10  # Número de termos que você quer na série

# Inicializa os dois primeiros termos
a, b = 0, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b