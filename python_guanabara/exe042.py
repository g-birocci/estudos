n1 = int(input("Digite um número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))

# Determinar o maior número
if n1 >= n2 and n1 >= n3:
    maior = n1
elif n2 >= n1 and n2 >= n3:
    maior = n2
else:
    maior = n3

# Determinar o menor número
if n1 <= n2 and n1 <= n3:
    menor = n1
elif n2 <= n1 and n2 <= n3:
    menor = n2
else:
    menor = n3

print(f"O maior número é {maior} e o menor é {menor}.")
