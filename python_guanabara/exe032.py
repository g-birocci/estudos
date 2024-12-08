nome = str(input("Digite o nome completo: ").strip()).lower()

teste = nome.find("silva")

if teste == 0:
    print("Está frase tem SILVA.")
else:
    print("Está nome não tem SILVA.")