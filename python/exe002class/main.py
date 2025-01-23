from conta import ContaBancaria
from random import randint

obj_conta = ContaBancaria

print("Bem-vindo ao Birocci Bank")
contas = {}

while True:
    print("""\nSelecione o que deseja fazer:
    1 - Abrir Conta
    2 - Fazer Saque
    3 - Fazer Depósito
    4 - Consultar Saldo
    5 - Exibir Histórico
    6 - Sair
    """)
    opcao = input("Digite a opção desejada: ").strip()

    if opcao == "1":
        nome = input("Digite o seu nome e sobrenome: ").strip().title()
        if nome:
            numero_conta = randint(1000, 9999)
            contas[numero_conta] = ContaBancaria(nome)
            print(f"Conta criada com sucesso!\nTitular: {nome}\nNúmero da Conta: {numero_conta}")
        else:
            print("Erro: Nome inválido.")

    elif opcao == "2":
        numero_conta = int(input("Digite o número da sua conta: "))
        if numero_conta in contas:
            valor = float(input("Digite o valor que deseja sacar: R$ "))
            contas[numero_conta].sacar(valor)
        else:
            print("Erro: Conta não encontrada.")

    elif opcao == "3":
        numero_conta = int(input("Digite o número da sua conta: "))
        if numero_conta in contas:
            valor = float(input("Digite o valor que deseja depositar: R$ "))
            contas[numero_conta].depositar(valor)
        else:
            print("Erro: Conta não encontrada.")

    elif opcao == "4":
        numero_conta = int(input("Digite o número da sua conta: "))
        if numero_conta in contas:
            saldo = contas[numero_conta].consultar_saldo()
            print(f"Saldo atual: R${saldo:.2f}")
        else:
            print("Erro: Conta não encontrada.")

    elif opcao == "5":
        numero_conta = int(input("Digite o número da sua conta: "))
        if numero_conta in contas:
            contas[numero_conta].exibir_historico()
        else:
            print("Erro: Conta não encontrada.")

    elif opcao == "6":
        print("Obrigado por utilizar o Birocci Bank. Até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
