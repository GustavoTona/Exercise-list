'''
Faça um programa que leia 5 números e informe o maior número.
'''

maior_numero = 0

for i in range(5):
    numero = int(input(f"Digite o {i+1}º número: ")) # +1 para interar o input 
    if numero > maior_numero:
        maior_numero = numero

print("O maior número digitado foi:", maior_numero)