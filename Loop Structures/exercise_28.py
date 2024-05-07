'''

Faça um programa que calcule o valor total investido por um colecionador em sua coleção de CDs 
e o valor médio gasto em cada um deles. O usuário deverá informar a quantidade de CDs e o valor 
para em cada um.

'''

qtd_cds = int(input("Digite o número de cds: "))
    
total_cds = 0
    
    # Laço para coletar a quantidade de cds
for i in range(1, qtd_cds + 1):
        cds = int(input(f"Digite a preço do CD {i}: "))
        total_cds += cds  # Acumula o total de cds
    
    # Calcula a média de cds
media_cds = total_cds / qtd_cds

    # Mostra a média
print(f"O valor médio gasto por CD é: R${media_cds:.2f}")
print(f"O valor gasto total é: R${total_cds:.2f}")
