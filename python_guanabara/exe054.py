from random import randint
from time import sleep
jogo = ("PEDRA","PAPEL","TESOURA")

print('''--- Vamos jogar ---
    [0] PEDRA
    [1] PAPEL    
    [2] TESOURA 
    ''')

op = int(input("QUal é a sua jogada? "))
desktop = randint(0, 2)

print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PÔ")
sleep(2)
print( "-=" * 10)

print(f"O notebook jogou: {jogo[desktop]}")
print(f"Vc jogou: {jogo[op]}")
print("-==-" *10)

if desktop == 0:
    if op == 0:
        print("Empate !!!")
        print("-==-" *10)
    elif op == 1:
        print("Vc venceu !!!")
        print("-==-" *10)
    elif op == 2:
        print("Desktop ganhou !!!")
        print("-==-" *10)

elif desktop == 1:
    if op == 0:
        print("Desktop ganhou !!!")
        print("-==-" *10)
    elif op == 1:
        print("Empate !!!")
        print("-==-" *10)
    elif op == 2:
        print("Vc venceu !!!")
        print("-==-" *10)

elif desktop == 2:
    if op == 0:
        print("Vc ganhou !!!")
        print("-==-" *10)
    elif op == 1:
        print("Desktop ganhou !!!")
        print("-==-" *10)
    elif op == 2:
        print("Empate")
        print("-==-" *10)
        