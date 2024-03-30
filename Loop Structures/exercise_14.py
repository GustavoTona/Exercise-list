'''

Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de números pares
e a quantidade de números impares.

'''
#inicia a contagem de numeros
pares = 0
impares = 0

for i in range(10):
    numero = int(input("Digite o {}º número inteiro: ".format(i + 1)))
    if numero % 2 == 0: # Se o resto da divisão por 2 for zero, o número é par, caso contrário, é ímpar.
        pares += 1 #incrementar os pares
    else:
        impares += 1 #incrementar os impares

print("Quantidade de números pares:", pares)
print("Quantidade de números ímpares:", impares)


