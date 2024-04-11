'''

Faça um programa que mostre todos os primos entre 1 e N sendo N um número inteiro fornecido 
pelo usuário. O programa deverá mostrar também o número de divisões que ele executou para 
encontrar os números primos. Serão avaliados o funcionamento, o estilo e o número de testes
(divisões) executados.

'''

num = int(input('Digite o número inteiro: '))

def primo(num):
    if num <= 1:
        return False, []  # Retorna False e uma lista vazia se o número for menor ou igual a 1
    
    divisores = []  # Lista para armazenar os divisores
    for i in range(2, num):
        if num % i == 0:
            divisores.append(i)  # Adiciona o divisor à lista

    if divisores:
        return False, divisores  # Retorna False e a lista de divisores se houver algum divisor encontrado
    return True, []  # Retorna True e uma lista vazia se não houver divisores

is_primo, divisores = primo(num)

if is_primo:
    print('Este número é primo')
else:
    print(f'Este número não é primo e é divisível por: {divisores}')

    

    
   