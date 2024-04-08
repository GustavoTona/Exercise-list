'''

Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
 Um número primo é aquele que é divisível somente por ele mesmo e por 1.

'''

num = int(input('Digite o número inteiro: '))

def primo(num):
    if num <= 1:  # Verifica se o número é menor ou igual a 1
        return False  # Se for menor ou igual a 1, não é primo

    for i in range(2, num):
        if num % i == 0:  # Verifica se o número é divisível por algum número diferente de 1 e ele mesmo
            return False  # Se for divisível, não é primo
    return True  # Se não for divisível por nenhum número diferente de 1 e ele mesmo, é primo

if primo(num):
    print('Este número é primo')
else:
    print('Este número não é primo')

    

    
   