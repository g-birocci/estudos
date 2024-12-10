from random import randint #importanto apenas radiante
from time import sleep #cria o efeito que o computador está pensando (222)
desktop = randint(0, 5) #Valor que o pc vai pensar

print("-=-" *10)
print("Vou pensar em um numero entre 0 e 5")
print("-=-" *10)

player = int(input("Tente advinhas o numero que o PC pensou: "))
print("Processando...")
sleep(3) #(222)

if player == desktop: #vereficando de o valor está correto
    print("Parabens vc ganhou !!!")
else:
    print("GANHEI, vc perdeu !!!")

