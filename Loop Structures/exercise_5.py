'''
Altere o programa anterior permitindo ao usuário informar as populações e as taxas de crescimento iniciais. 
Valide a entrada e permita repetir a operação.
'''


populacao_a = int(input('Habitantes da Cidade A: '))
while populacao_a < 0:
    print("População deve ser acima de 0")
    populacao_a = int(input('Habitantes da Cidade A: '))

populacao_b = int(input('Habitantes da Cidade B: '))
while populacao_b < 0:
    print("População deve ser acima de 0")
    populacao_b = int(input('Habitantes da Cidade B: '))

taxa_crescimento_a = float(input('Taxa de crescimento da Cidade A: '))
taxa_crescimento_b = float(input('Taxa de crescimento da Cidade B: '))

taxa_crescimento_a = taxa_crescimento_a / 100
taxa_crescimento_b = taxa_crescimento_b / 100

anos = 0
while populacao_a < populacao_b:
        populacao_a *= (1 + taxa_crescimento_a)
        populacao_b *= (1 + taxa_crescimento_b)
        anos += 1

print(f"Número de anos necessários para A ultrapassar ou igualar B: {anos}")



