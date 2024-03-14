'''Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:
o produto do dobro do primeiro com metade do segundo .
a soma do triplo do primeiro com o terceiro.
o terceiro elevado ao cubo. '''

A, B = map(int, input('Coloque 2 números inteiros: ').split())

C = float(input('Coloque 1 número real: '))

produto = (A * 2) * (B / 2)
soma = (A *3) + C
cubo = C ** 3

print("O produto do dobro do primeiro com metade do segundo é:", produto)
print("A soma do triplo do primeiro com o terceiro é:", soma)
print("O terceiro elevado ao cubo é:", cubo)