'''
Faça um Programa que leia três números e mostre-os em ordem decrescente.
'''

num_1 = int(input('Digite um valor: '))
num_2 = int(input('Digite um valor: '))
num_3 = int(input('Digite um valor: '))

lista = [num_1, num_2, num_3]

#Sort para reorganizar a lista em crescente, e o reverse para virar descrente
lista.sort(reverse=True)

print(lista)

