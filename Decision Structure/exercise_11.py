'''
As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores e lhe contraram para desenvolver o programa que calculará os reajustes.
Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
salários até R$ 280,00 (incluindo) : aumento de 20%
salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
salários de R$ 1500,00 em diante : aumento de 5% Após o aumento ser realizado, informe na tela:
o salário antes do reajuste;
o percentual de aumento aplicado;
o valor do aumento;
o novo salário, após o aumento.
'''

salario = int(input('Qual o seu salário? '))

if salario < 280:
    porcentagem = 20
    aumento = salario + (salario * 0.20)
    
elif salario < 700:
    porcentagem = 15
    aumento = salario + (salario * 0.15)

elif salario < 1500 :
    porcentagem = 10
    aumento = salario + (salario * 0.10)

else:
    porcentagem = 5
    aumento = salario + (salario * 0.05)

valor_aumento = salario - aumento

print(f'Seu salário atual: {salario}')
print(f'Seu percentual de aumento é: {porcentagem}%')
print(f'Valor do aumento: {abs(valor_aumento)}') # abs para remover o sinal negativo
print(f'Salario total: {aumento: .2f}')