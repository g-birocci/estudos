lista_produto = []
prices = 0
sair = True

def total(lista_produto):
    total = 0
    for produto in lista_produto:
        total += produto["price"]
    return total

def produto_mil(lista_prdoduto):
    cont = 0
    for produto in lista_prdoduto:
        if produto["price"] > 1000:
            cont += 1
    return cont


def mais_barato(lista_produto):
    # Verifica se a lista não está vazia
    if not lista_produto:
        return None 
    barato = lista_produto[0]
    
    for produto in lista_produto:
        if produto["price"] < barato["price"]:
            barato = produto
    
    return barato

while True:
    while True:
        name = str(input("What is the name of the product? ")).upper().strip()
        if name == "":
            print("Digite o nome do produto! ")
        else:
            break

    while sair:
        try:
            price = float(input("What is the price of the product? "))
            if price < 0:
                print("The price can only be a positive number!")
            else:
                sair = False

        except ValueError:
            print("Invalid input!")
        
    lista_produto.append({"name": name, "price": price})

    sair = str(input("Quer continuar [S/N] ? ")).upper().strip()

    if sair == "N":
        break
    else:
        print("Bem-vindo")


total_comprado = total(lista_produto)
print(f"O tatal da compra ficou por {total_comprado}£.")
produto = produto_mil(lista_produto)
print(f"Teve no total {produto} custando mais de 1000£")
produto_mais_batato = mais_barato(lista_produto)
print(f"O produto mais barato é {produto_mais_batato}.")
