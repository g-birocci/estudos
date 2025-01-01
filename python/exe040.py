def calcula_desconto(preco, desconto):
    desconto = 20
    preco_novo = preco - (preco * desconto)/100
    return preco_novo

preco = float(input("Digite o valor do produto: "))

if preco >= 100:
    desconto = True
    valor = calcula_desconto(preco, desconto)
    print(f"O valor com desconto vai ficar por {valor}")
else:
    print(f"O valor do produto é {preco}")