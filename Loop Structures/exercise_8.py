'''
Faça um programa que leia 5 números e informe o maior número.
'''

soma = 0 #

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    soma += numero

media = soma / 5

print("A soma dos números é:", soma)
print("A média dos números é:", media)