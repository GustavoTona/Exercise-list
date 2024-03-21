'''
Faça um Programa para leitura de três notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e presentar:
A mensagem "Aprovado", se a média for maior ou igual a 7, com a respectiva média alcançada;
A mensagem "Reprovado", se a média for menor do que 7, com a respectiva média alcançada;
A mensagem "Aprovado com Distinção", se a média for igual a 10.

'''

nota_1, nota_2, nota_3 = map(int, input().split())

media = (nota_1 + nota_2 + nota_3) / 3 

if media == 10:
    print('Aprovado com distinção')
elif media >= 7:
    print('Aprovado.')
else:
    print('Reprovado.')
