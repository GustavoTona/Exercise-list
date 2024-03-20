'''
Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
Desconto do IR:
Salário Bruto até 900 (inclusive) - isento
Salário Bruto até 1500 (inclusive) - desconto de 5%
Salário Bruto até 2500 (inclusive) - desconto de 10%
Salário Bruto acima de 2500 - desconto de 20% Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
'''

valor = int(input('Qual o valor da hora de trabalho: '))
hora = int(input('Quantas horas de trabalhadas no mês: '))


salario_bruto = hora * valor

if salario_bruto < 900:
    porcentagem = ('insento')
    ir = 0
    inss = salario_bruto * 0.10
    
elif salario_bruto < 1500:
    porcentagem = 5
    ir = salario_bruto * 0.05
    inss = salario_bruto * 0.10

elif salario_bruto < 2500 :
    porcentagem = 10
    ir = salario_bruto * 0.10
    inss = salario_bruto * 0.10
    
else:
    porcentagem = 20
    ir = salario_bruto * 0.20
    inss = salario_bruto * 0.10

salario_liquido = salario_bruto - ir - inss
total_desconto =   ir + inss
fgts = salario_bruto * 0.11


print(f'Salário Bruto: ({hora} * {valor}): R$ {salario_bruto}')
print(f'(-) IR ({porcentagem}%): R${ir: .2f}')
print(f'(-) INSS ({porcentagem}%): R${inss: .2f}')
print(f'FGTS: R$ {fgts}') # abs para remover o sinal negativo
print(f'Total de descontos: R${total_desconto: .2f}')
print(f'Salario Liquido: R${salario_liquido: .2f}')
