import random
tentativa = random.randint(1, 10)  # Gera um número inteiro aleatório entre 1 e 10
vezes = 0
sair = True
while sair:
    jogador = int(input("Tente adivinha o numero que o computador pensou: "))
    if jogador == tentativa:
        print("VC acertou.")
        print(f"Vc teve {vezes} tentativas até acerta.")
        break
    else: 
        sair = True
    vezes = vezes + 1

