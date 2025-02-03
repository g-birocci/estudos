from random import randint
while True:
    n = int(input("Digite um numero: "))
    op = str(input("PAR ou ÌMPAR? [P/I] ")).upper().strip()
    desktop = randint(1, 10)
    print(f"O Computador escolheu {desktop} e vc {n}")

    soma = n + desktop
    
    if soma % 2 == 0:
        print("Deu PAR!")
        if op == "P":
            print("Você venceu! 😃\n")
        else:
            print("Você perdeu! 😞\n")
            break
    else:
        print("Deu ÍMPAR!")
        if op == "I":
            print("Você venceu! 😃\n")
        else:
            print("Você perdeu! 😞\n")
            break

print("=== Fim do jogo. Obrigado por jogar! ===")