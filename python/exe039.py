def verificar_clima(temperatura, tempo, chuva):
    if 15 <= temperatura <= 30 and chuva == "N" and tempo == "S":
        return "O tempo está bom para correr."
    else:
        return "Caminhada não segura."

# Entrada de dados
temperatura = int(input("Digite a temperatura: "))
tempo = input("Como está o tempo? [S - Sol / N - Nublado]: ").strip().upper()
chuva = input("Está chovendo? [S - Sim / N - Não]: ").strip().upper()

# Chamada da função e exibição do resultado
resultado = verificar_clima(temperatura, tempo, chuva)
print(resultado)
