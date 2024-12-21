soma = 0
for n in range(1, 500):
  if n % 3 == 0:
    z = n
    if z % 2 != 0:
        print(z)
        soma = soma + z
print(f"A soma de todos esses numeros são {soma}")

