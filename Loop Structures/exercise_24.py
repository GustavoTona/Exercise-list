'''

Faça um programa que calcule o mostre a média aritmética de N notas.

'''

    # Solicita ao usuário o número de notas
num_notas = int(input("Digite a quantas notas serão: ")) 
    # Lista para armazenar as notas
notas = []
    # Laço para coletar as notas
for i in range(1, num_notas + 1):
        nota = float(input(f"Digite a nota {i}: "))
        notas.append(nota)
    # Calcula a média aritmética
media = sum(notas) / num_notas
    # Mostra a média
print(f"A média aritmética é: {media:.2f}")
    
   