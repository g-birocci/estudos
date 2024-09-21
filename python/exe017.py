print("Digite os itens para a lista !!!")
lista = []
is_valid = False
while is_valid == False:
    if len(lista) >= 10:
            print("Só pode ter 10 itens na lista!")
            is_valid = True
            break
    itens = input("Digite um item para a lista (ou digite 'sair' para finalizar): \n")
    if itens.lower() == "sair":
        break
    lista.append(itens)
    continuar = input("Deseja continuar? Digite 'sim' para continuar ou 'remover' para remover um item: \n")
    if continuar.lower() == "sim":
        continue    
    elif continuar.lower() == "remover":
        if lista:
            item_to_remove = input("Digite o item que deseja remover: ")
            if item_to_remove in lista:
                lista.remove(item_to_remove) 
            else:
                print("O item não está na lista.")
        else:
            print("A lista está vazia, nada para remover.")    
    else:
        print("Input errado, programa encerrado.")
        break
for c in lista:
    print(c)