print("Digite 6 numeros inteiros")
soma = 0
for n in range(0, 6):
    n = int(input("Digite um numero: "))
    if n % 2 == 0:
        soma = soma + n
print(f"A soma dos numeros pares é {soma}")
