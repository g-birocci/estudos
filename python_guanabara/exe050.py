from datetime import date
ano_atual = date.today()

print("--- Descubra a sua categoria ---")
ano_nasc = int(input("Digite o seu ano de nascimento: "))

idade = ano_atual.year - ano_nasc
print(f"Você tem {idade} anos.")

if idade <= 9:
    print("Sua categoria é MIRIM.")
elif idade <= 14:
    print("Sua categoria é INFANTIL")
elif idade <= 19:
    print("Sua categocia é JUNIOR")
elif idade == 20:
    print("Sua categoria é SÊNIOR")
else:
    print("Sua categoria é MASTER")

