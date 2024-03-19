'''
Faça um Programa que pergunte em que turno você estuda. Peça para digitar M-matutino ou V-Vespertino ou N- Noturno. 
Imprima a mensagem "Bom Dia!", "Boa Tarde!" ou "Boa Noite!" ou "Valor Inválido!", conforme o caso.
'''

turno = input('Em que turno voce estuda? (Matutino/Vespertino ou Noturno? ')

if turno == 'atutino': 
    print('Bom Dia!')
elif turno == 'vespertino':
    print('Boa Tarde!')
else: 
    print('Boa Noite!')


