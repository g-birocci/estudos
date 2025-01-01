soma = 0
cont = 0
for n in range(1, 500):
  if n % 3 == 0:
    cont = cont + 1
    z = n
    if z % 2 != 0:
        print(z)
        soma = soma + z
print(f"A soma de todos os {cont} valores solicitados é {soma}")

