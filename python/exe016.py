print("Digite os ingredientes na lista !!!")
lis_ta = []
for i in range(10):
    sair = False
    while not sair:
        itens = input("Digite os itens: ").strip().lower()
        remo = input("Deseja continuar ou remover itens [Sim/Remover]")
        if remo == "remover":
            Remo = input("Qual itens deseja removover? ")
            lis_ta.remove(remo)
            print(lis_ta)
        else:
            if itens == "sair":
                sair = True
                print("Lista final de ingredientes:", lis_ta)
                break
            else:
                lis_ta.append(itens)

