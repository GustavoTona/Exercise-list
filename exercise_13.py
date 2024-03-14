'''Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
Para homens: (72.7*h) - 58
Para mulheres: (62.1*h) - 44.7'''

h = float(input('Qual a sua altura? '))
genero = input('Você é homem ou mulher? ')

if genero.lower() == "homem":  #lower para converter para minuscula para comparar com string
    homens = (72.7 * h) - 58
    print("O peso ideal para homens é: ", format(homens, '.1f'))

elif genero().lower() == "mulher": #lower para converter para minuscula para comparar com string
    mulheres = (62.1 * h) - 44.7
    print("O peso ideal para mulheres é: ",format(mulheres, '.1f'))

else:
    print('Genero não reconhecido, escolha entre homem e mulher')