print("-" * 30)
print("----- Lista de produtos ------")
print("-" * 30)
lista_compras = (
    ("Arroz", 5.99),
    ("Feijão", 8.50),
    ("Macarrão", 3.25),
    ("Óleo", 7.30),
    ("Açúcar", 4.10),
    ("Café", 10.20)
)

# Exibindo a lista de compras
print("Lista de Compras:")
for produto, preco in lista_compras:
    print(f"{produto:.<20}: R$ {preco:.2f}")
