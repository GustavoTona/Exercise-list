'''
Faça um Programa que leia três números e mostre o maior e o menor deles.
'''

A, B, C = map(int, input().split())

maior = max(A, B , C) # max para achar o maior
menor = min(A ,B , C)

print(f'Maior número é: {maior}')
print(f'Menor número é: {menor}')



