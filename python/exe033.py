import csv

reserva ={} 

def add_reserva():

    while True:
        print("Fazer reserva!")
        client_id = input("ID usuario (NIF)")
        nome = input("Digite o seu nome: ")
        destino = input("Digite a cidade: ")
        n_reservas = input("Digite o numeros de reservas: ")

        reserva[client_id] = {"nome": nome, "destino": destino, "n_reservas": n_reservas} 

        adicionar_mais = input("Quer adicionar mais um clinete: ")
        if adicionar_mais.lower() != "s":
            break

def consultar_reserva():

    print("Consultar reserva! ")
    client_id = input("Digite o ID do cliente que deseja pesquisar: ")
    for client_id in reserva.items():
        print(f"{client_id}")
        


def listar_reservas ():
    for reservas in reserva:
        print(reservas)

sair = True
while sair:

    print("BIROCCI RESERVAS!")
    print("1--ADCIONAR RESERVA: ")
    print("2--CONSULTAR RESERVA: ")
    print("3--LISTAR TODAS RESERVAS: ")
    print("4--sAIR")

    op = int(input("Digite a opção desejada: "))

    match op:

        case 1:
            add_reserva()
        
        case 2:
            consultar_reserva()

        case 3:
            listar_reservas()
        
        case 4:
            sair = False

        case _: 
            print("Opção invalida") 