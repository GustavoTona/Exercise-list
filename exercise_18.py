"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de
 Internet (em Mbps), calcule e informe o tempo aproximado de download do arquivo usando este link 
 (em minutos).
"""

tamanho_arquivo = float(input("Digite o tamanho do arquivo em MB: "))
velocidade_internet= float(input("Digite a velocidade da internet em Mbps: "))
# Calcula o tempo de download em segundos
tempo_download_segundos = (tamanho_arquivo * 8) / velocidade_internet

# Calcula minutos e segundos
minutos = int(tempo_download_segundos // 60)
segundos = int(tempo_download_segundos % 60)

print(f"O tempo aproximado de download do arquivo é de: {minutos} minutos e {segundos} segundos")
