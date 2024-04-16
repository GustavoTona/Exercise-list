'''

Numa eleição existem três candidatos. Faça um programa que peça o número total de eleitores. 
Peça para cada eleitor votar e ao final mostrar o número de votos de cada candidato.

'''

quant_pessoas = int(input("Digite a quantidade de pessoas: ")) 
    # Lista para armazenar as idades
notas = []
    # Laço para coletar as idades
for i in range(1, quant_pessoas + 1):
        nota = float(input(f"Digite a idade {i}: "))
        notas.append(nota)

    # Calcula a média aritmética 
media = sum(notas) / quant_pessoas

if media < 25:
    print(f"A média da turma é: Jovem")
elif media < 60:
    print(f"A média da turma é: Adulta")
else:
     print(f"A média da turma é: Idosa")

    
   