nota = float(input("Digite a sua nota: "))

if nota >= 0:
    if nota <=10:
        if nota >= 6:
            print("Você foi aprovado. ")
        if nota <6:
            print("Você foi reprovado.")
    else:
        print("Nota não aceita.")
else:
    print("Nota não aceita.")   