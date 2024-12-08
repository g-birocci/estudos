n = str(input("Digite o seu nome completo: ").lower()).strip()
nome = n.split()

print(f"Your fist name is: {nome[0].upper()}")

print(f"Your last name is: {nome[-1].upper()}")