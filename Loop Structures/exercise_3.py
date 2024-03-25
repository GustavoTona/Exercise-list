'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd';
'''
nome = input("Informe um nome: ")
while len(nome) <= 3:
    print("O nome deve ter mais de 3 caracteres.")
    nome = input("Informe um nome: ")

# Validar a idade
idade = int(input("Informe a idade: "))
while not 0 <= idade <= 150:
    print("A idade deve estar entre 0 e 150.")
    idade = int(input("Informe a idade: "))

# Validar o salário
salario = float(input("Informe o salário: "))
while salario <= 0:
    print("O salário deve ser maior que zero.")
    salario = float(input("Informe o salário: "))

# Validar o sexo
sexo = input("Informe o sexo (f/m): ").lower()
while sexo not in ('f', 'm'): # not in - se nao tiver na lista f ou m o programa mostra erro 
    print("O sexo deve ser 'f' ou 'm'.")
    sexo = input("Informe o sexo (f/m): ").lower()

# Validar o estado civil
estado_civil = input("Informe o estado civil (s/c/v/d): ").lower()
while estado_civil not in ('s', 'c', 'v', 'd'): # not in - se nao tiver na lista as letras o programa mostra erro 
    print("O estado civil deve ser 's', 'c', 'v' ou 'd'.")
    estado_civil = input("Informe o estado civil (s/c/v/d): ").lower()

# Imprimir informações válidas
print("\nInformações válidas:")
print("Nome:", nome)
print("Idade:", idade)
print("Salário:", salario)
print("Sexo:", sexo)
print("Estado Civil:", estado_civil)
