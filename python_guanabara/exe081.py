lista_produto = []
sair = True
prices = 0

def total(prices):
    for prices in lista_produto:
        if prices["price"]:
            prices = prices + price
    return prices
    
while True:
    while sair:
        name = str(input("What is the name of the product? ")).upper().strip()
        if name == "":
            sair = True
        else:
            sair = False


    while sair:
        price = float(input("What is the price of the product? ").strip())
        if price < 0:
            print("The price can only be a positive number!")
            sair = True
        elif price == "":
            print("The price went black")
            sair = True
        else:
            sair = False
        
    lista_produto.append[{"name": name, "price": price}]

    sair = str(input("Quer continuar [S/N] ? "))

    if sair == "N":
        break

print()


