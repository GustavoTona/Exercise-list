'''

Faça um programa que calcule o número médio de alunos por turma. 
Para isto, peça a quantidade de turmas e a quantidade de alunos para cada turma. 
As turmas não podem ter mais de 40 alunos.

'''

num_turmas = int(input("Digite o número de turmas: "))
    
    # Verifica se o número de turmas é positivo
    
total_alunos = 0
    
    # Laço para coletar a quantidade de alunos em cada turma
for i in range(1, num_turmas + 1):
        while True:  # Loop infinito que só quebra quando um valor válido é fornecido
            alunos = int(input(f"Digite a quantidade de alunos na turma {i}: "))
            if 1 <= alunos <= 40:
                break  # Sai do loop se o número de alunos for válido
            else:
                print("Cada turma deve ter entre 1 e 40 alunos.")
        
        total_alunos += alunos  # Acumula o total de alunos
    
    # Calcula a média de alunos por turma
media_alunos = total_alunos / num_turmas
    
    # Mostra a média
print(f"O número médio de alunos por turma é: {media_alunos:.2f}")

    
   