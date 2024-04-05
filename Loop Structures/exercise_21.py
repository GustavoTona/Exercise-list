'''

Faça um programa que peça um número inteiro e determine se ele é ou não um número primo.
 Um número primo é aquele que é divisível somente por ele mesmo e por 1.

'''


num = int(input('Digite o número inteiro: '))

def primo(num):
    for i in range (2, num):
        if num % i == 0:
            return False
    return True


if primo(num):
    print('Este número é primo')
else: 
    print('Este numero não é primo')

    

    
   