'''
Faça um programa que peça uma nota, entre zero e dez. 
Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

'''

while True:
    nota = float(input("Digite uma nota entre zero e dez: "))
    
    if 0 <= nota <= 10:
        print("Nota válida:", nota)
        break
    else:
        print("Nota inválida. Por favor, digite novamente.")