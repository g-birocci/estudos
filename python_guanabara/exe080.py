lista = []
cont = 0

def maior_idade(cont):
    for pessoa in lista:
        if pessoa["idade"] > 18:
            cont += 1
    return cont

def homen(cont):
    for pessoa in lista:
        if pessoa["sexo"] == "M":
            cont += 1
    return cont

def mulher(cont):
    for pessoa in lista:
        if pessoa["sexo"] == "F":
            if pessoa["idade"] < 20:
                cont += 1
    return cont

while True:
    while True:
        idade = int(input("Digite a idade: ").strip())          
        if idade > 0:
            break
        else:
            print("Erro: A idade deve ser um número positivo. Tente novamente.")

    while True:   
        sexo = str(input("[M/F]: ")).upper().strip()
        if sexo == "M":
            break
        elif sexo == "F":
            break
        else:
            print("O sexo só pode ser M - Masculino ou F - feminino")

    lista.append({"idade": idade, "sexo": sexo})

    sair = str(input("Quer continuar? [S/N] ")).upper().strip()  # Remover .split()

    if sair == "N":
        break

maior = (maior_idade(cont))
print(f"No total foram adicionado {maior} pessoas com mais de 18 anos.")
H = (homen(cont))
print(f"No total foram cadastrados {H} homens.")

M = (mulher(cont))
print(f"No total foram cadastrados {M} mulheres com menos de 20 anos.")