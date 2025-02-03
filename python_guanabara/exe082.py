print(" --- Bem Vindo ---")
valor = int(input("Qual o valor que você quer sacar? "))
total = valor

celula = 100
cont_n = 0

while total > 0:
    if total >= celula:
        total -= celula
        cont_n += 1
    else:
        if cont_n > 0:
            print(f"Total de {cont_n} cédulas de {celula}£")
        if celula == 100:
            celula = 50
        elif celula == 50:
            celula = 20
        elif celula == 20:
            celula = 10
        elif celula == 10:
            celula = 5
        elif celula == 5:
            celula = 1
        cont_n = 0
if cont_n > 0:
    print(f"Total de {cont_n} cédulas de {celula}£")
