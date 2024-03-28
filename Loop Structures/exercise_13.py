'''

Faça um programa que peça dois números, base e expoente, calcule e mostre o primeiro
 número elevado ao segundo número. Não utilize a função de potência da linguagem.

'''

base = int(input("Digite um número base: "))
expoente = int(input("Digite um número para expoente: "))

resultado = base # iniciar a variavel com o valor da base
for _ in range(1, expoente): # Começa com um e intera até o expoente

    resultado *= base #Base dentro do loop multiplica o resultado pela

print("O resultado de", base, "elevado a", expoente, "é igual:", resultado)



