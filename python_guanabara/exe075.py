sair = True
soma = 0
while sair:
    n = int(input("Digite um numero: \n"))
    soma += n
    stop = str((input("Deseja continuar? [S/N]\n"))).upper()
    if stop == "S":
        sair = True
    else:
        print(f"A soma de todos os valores inseridos foi {soma}.")
        sair = False


