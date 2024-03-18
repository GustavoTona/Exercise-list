'''
Faça um Programa que verifique se uma letra digitada é vogal ou consoante.
'''

letra = input()
vogais = 'aeiou'

#lower padronizar se for maisculo ou minuscolo
if letra.lower() in vogais: # in para verificar um determinado valor em uma sequencia
    print('Vogal')
else:
    print('Consoante')

