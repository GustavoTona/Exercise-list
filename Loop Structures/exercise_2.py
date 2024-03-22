'''
Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome 
do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.
'''

usuario = input("Crie seu usuario: ")

while True:
    
    senha = input("Crie sua senha: ")
    
    if senha != usuario: #usuario diferente de senha
        print("Senha válida!")
        break
    else:
        print("Senha inválida. Por favor, digite novamente.")