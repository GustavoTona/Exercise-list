'''

Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

'''

print("Responda 'sim' ou 'não' para as seguintes perguntas:")

perguntas = [
    "Telefonou para a vítima?",
    "Esteve no local do crime?",
    "Mora perto da vítima?",
    "Devia para a vítima?",
    "Já trabalhou com a vítima?"
]

respostas_positivas = 0

# Perguntar as perguntas
for pergunta in perguntas:
    resposta = input(pergunta + " ").lower()
    # se a repostar for sim adicionar mais um
    if resposta == "sim":
        respostas_positivas += 1

# Emitir a classificação
if respostas_positivas == 2:
    print("Você é considerado(a) SUSPEITO(A).")
elif 3 <= respostas_positivas <= 4:
    print("Você é considerado(a) CÚMPLICE.")
elif respostas_positivas == 5:
    print("Você é considerado(a) ASSASSINO(A).")
else:
    print("Você é considerado(a) INOCENTE.")