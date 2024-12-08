cidade = str(input("Digite o nome da sua cidade: ").strip()).lower()

teste = cidade.find("santo")

if teste == 0:
    print("Está frase tem santo.")
else:
    print("Está Frase não tem santo.")