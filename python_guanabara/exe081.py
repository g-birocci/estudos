lista_produto = []
prices = 0
sair = True
def total(lista_produto):
    total = 0
    for produto in lista_produto:
        total += produto["price"]
    return total

def mais_barato(lista_produto):
    # Verifica se a lista não está vazia
    if not lista_produto:
        return None  # Retorna None se não houver produtos na lista
    
    # Inicializa com o primeiro produto como o mais barato
    barato = lista_produto[0]
    
    for produto in lista_produto:
        # Verifica se o preço do produto atual é menor que o do mais barato
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

    sair = str(input("Quer continuar [S/N] ? "))

    if sair == "N":
        break

total_comprado = total(lista_produto)
print(f"O tatal da compra ficou por {total_comprado}£.")
