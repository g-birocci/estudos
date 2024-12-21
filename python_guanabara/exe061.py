import math
print("Vereficar se é um numero primo")
n = int(input("Digite um numero inteiro: "))

if n > 1:
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i != 0:
            print(f"O numero {n} é um numero primo.")
        else:
            print(f"o numero {n} não é primo.")
else:
    print("Não existe numero primo se ele for negativo.")