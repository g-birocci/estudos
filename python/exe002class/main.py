from conta_bancaria import Conta_banco
from random import randint

obj_conta = Conta_banco

print("Bem-Vindo")
print("-*-" * 40)
sair = True
while sair:
    print("Bem-vindo ao Birocci Bank")
    print('''Selecione o que vc deseja fazer
            1 -- Abrir Conta
            2 -- Fazer saque
            3 -- Fazer deposito
            4 -- Ver saldo
            5 -- Sair
          ''')
    op = str(input("Digite a opção desejada: "))

    match op:
        case "1":
            print("Abrir conta.")
            nome_ok = True
            while nome_ok:
                nome = input("Digite o Seu nome e sobrenome: ").strip().upper()
                if nome:
                    nome_ok = False               
                else:
                    print("Erro: O nome não deve ser em branco. Tente novamente.")
            conta = randint(1000, 9999)
            saldo = 0
            conta_nova = obj_conta(nome, conta, saldo)
            
            print("Sua conta foi criada ;)")
            print(f"Seu nome: {nome}")
            print(f"Numero de conta: {conta}")
            print(f"Saldo: £{saldo}\n")


        case "2":
            conta_digitada = int(input("Digite o numero da sua conta: "))
            valor_saque = float(input("Digite o valor que deseja retirar: "))
            obj_conta.saque(conta_digitada)

        #     pass

        #case "3":
         #   pass

        #case "4":
         #   pass

        case "5":
            sair = False
        
        case _:
            print("Opção invalida!")
