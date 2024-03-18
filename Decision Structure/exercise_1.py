# Faça um Programa que peça dois números e imprima o maior deles.

A, B = map(int, input().split())

if A > B: 
    print(f'O numero {A} é maior')
else: 
    print(f'O numero {B} é maior')