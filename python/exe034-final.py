import re
import random
dicionario = {}
saldo = []

def depositar_fundo():
    dinheiro = float(input("Digite a quantia que deseja depositar: "))
    saldo.append(dinheiro)
    print(f"Seu saldo atual é {saldo}")
    
def escolher_cavalo():

    desistir = True
    while desistir:
        print("----- Escolher cavalo -----")
        print("1--Azul")
        print("2--Vermelho")
        print("3--Rosa")
        print("4--Amarelo")
        print("Desistir aposta.")

        cavalo_escolhido = str(input("Escolha um cavalo: "))

        match cavalo_escolhido:
        
            case "1":
                cavalo_escolhido = 1
                break     
            case "2":
                cavalo_escolhido = 2
                break
            case "3":
                cavalo_escolhido = 3
                break
            case "4":
                cavalo_escolhido = 4
                break
            case _:
                escolher_cavalo()

def fazer_aposta():
    dinheiro_aposta = float(input("Digite a quantia que deseja apostar: "))
    return dinheiro_aposta
                
def atualizar_saldo():
    print("Em manutenção")

def simular_corrida():
    cavalos = ["1","2","3","4"]
    return random.choice(cavalos)
    



sair = True
while sair:

    print("----Menu----")
    print("1--Deseja depositar dinheiro. ")
    print("2--Deseja atualizar saldo. ")
    print("3--Escolher cavalo. ")
    print("4--Fazer aposta. ")
    print("5--Simular corrida ")
    print("6--Sair ")

    op = str(input("Digite o numero da opção desejada: "))

    match op:
        
        case "1":
            
            depositar_fundo()

        case "2":
            atualizar_saldo()

        case "3":
            escolher_cavalo()
        
        case "4":
            fazer_aposta()

        case "5":
            simular_corrida()

        case "6":
            sair = False
        case _:
            print("opção errada")

        

    
