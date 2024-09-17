print("Bem-vindo ao jogo da adivinhação!!!")
print("você tera que adivinhar um numero de 1, 50!!!")
print("vamos começar!!!")
import random 
max_t = 5
rodada = 1
ns = random.randint(1,50)

while rodada <= max_t :
    tentativa = int(input("Qual é seu numero?  "))
    rodada = rodada + 1
    
    if tentativa == ns:
        print("o numero esta certo. Parabens ")
        break
    else:
        if tentativa > ns:
            print("o numero é maior!")
        if tentativa < ns:
            print("o numero é menor!")
print("Você não conseguiu. ")