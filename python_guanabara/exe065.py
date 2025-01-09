print("Bem-vindo")
total_idade = 0
homen_mais_velho = 0
nome_velho = ""
mulheres_nova = 0
for i in range(1, 5):
    print(f"------- {i}ª pessoa -------") 
    nome = input("Digite o seu nome: ").strip().upper()
    idade = float(input("Digite a sua idade: "))
    sexo = input("Digite o seu sexo [F] [M]: ").strip().upper()
    total_idade += idade

    if i == 0 and sexo == "M":
        homen_mais_velho = idade
        nome_velho = nome
    if sexo == "M" and idade > homen_mais_velho:
        nome_velho = nome
        homen_mais_velho = idade
    if sexo == "F" and idade < 20:
        mulheres_nova += 1

media = total_idade / 4
print(f"A idade média do grupo é {media:.2f} anos")
print(f"O homen mais velhor é {nome_velho}.")
print(f"Existe {mulheres_nova} mulheres com menos de 20 anos.")
