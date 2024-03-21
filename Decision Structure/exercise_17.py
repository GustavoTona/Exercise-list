'''
Faça um Programa que peça um número correspondente a um determinado ano e em seguida informe se este ano é ou não bissexto.
'''

ano = int(input())

# Verifica se o ano é divisível por 4 e não é divisível por 100, ou se é divisível por 400.
if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
    print(f"O ano {ano} é bissexto.")
else:
    print(f"O ano {ano} não é bissexto.")