import math
print("Verificar se é um número primo")
n = int(input("Digite um número inteiro: "))

if n > 2:
    is_prime = True  # Assume que o número é primo
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:  # Se encontrar um divisor
            is_prime = False
            break
    
    if is_prime:
        print(f"O número {n} é um número primo.")
    else:
        print(f"O número {n} não é primo.")
else:
    print("Não existe número primo se ele for negativo ou menor que 2.")
