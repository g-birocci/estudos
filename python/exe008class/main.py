from lead import Lead
from customer import Cliente
from partner import Parceiro

print("Bem-vindo!")

while True:
    print('''
        Escolha a opção desejada!
        1 -- Cadastrar Cliente
        2 -- Cadastrar Líder
        3 -- Adicionar Parceiro
        4 -- Procurar Cliente
        5 -- Listar Líderes
        6 -- Listar Parceiros
        7 -- Sair
    ''')
    
    op = input("Escolha a opção desejada: ")

    if op == '1':
        nome = input("Digite o nome do cliente: ")
        print(f"Cliente {nome} cadastrado com sucesso!")
    elif op == '2':
        nome = input("Digite o nome do líder: ")
        print(f"Líder {nome} cadastrado com sucesso!")
    elif op == '3':
        nome = input("Digite o nome do parceiro: ")
        print(f"Parceiro {nome} adicionado com sucesso!")
    elif op == '4':
        nome = input("Digite o nome do cliente para procurar: ")
        print(f"Procurando cliente {nome}... (implementação futura)")
    elif op == '5':
        print("Listando líderes... (implementação futura)")
    elif op == '6':
        print("Listando parceiros... (implementação futura)")
    elif op == '7':
        print("Saindo do sistema. Até logo!")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.")
