sair = True
while sair:
    sexo = str(input("Digite o seu sexo: ")).upper()
    if sexo == "M":
        print("Sexo aceito")
        break
    elif sexo == "F":
        print("Sexo aceito")
        break
    else:
        print("Só é aceito [M] ou [F]")
        sair = True
