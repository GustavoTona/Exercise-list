# Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
# Calcule e mostre o total do seu salário no referido mês.
valor_hora = float(input("Quanto você ganha por hora?"))
hora_mes = int(input("Quantas horas trabalhada no mês?"))

resultado = hora_mes * valor_hora

print("Salário:",resultado,"R$")