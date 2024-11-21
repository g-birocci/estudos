lista_produtos = []

def total_venda(lista_produtos):
    total_venda = 0
    for produto in lista_produtos:
        total_venda += produto["preco"] * produto["quantidade_vendida"]
    return total_venda

def total_venda_produto(produto):
    return produto["preco"] * produto["quantidade_vendida"]

def produto_mais_vendido(lista_produtos):
    produto_mais_vendido = (0, '')
    for produto in lista_produtos:
        if produto["quantidade_vendida"] > produto_mais_vendido[0]:
            produto_mais_vendido = (produto["quantidade_vendida"], produto["nome"])
    return produto_mais_vendido

sair = True
while sair:

    print("\nMenu:")
    print("1-- Cadastrar produto")
    print("2-- Total de vendas de um produto")
    print("3-- Produto mais vendido")
    print("4-- Total de vendas")
    print("5-- Sair")

    opcao = int(input("Digite o número da opção desejada: "))

    if opcao == 1:
        nome = input("Nome do Produto: ").lower()
        preco = float(input("Digite o Preço do Produto: "))
        quantidade_vendida = int(input("Quantidade total de produto vendido: "))

        # Criando um novo dicionário para o produto
        produto = {
            "nome": nome,
            "preco": preco,
            "quantidade_vendida": quantidade_vendida
        }

        lista_produtos.append(produto)
        print("Produto cadastrado com sucesso!")

    elif opcao == 2:
        produto_procurado = input("Digite o nome do produto que deseja calcular: ").lower()
        total_vendido_do_produto = 0

        for produto in lista_produtos:
            if produto_procurado == produto["nome"]:
                total_vendido_do_produto = total_venda_produto(produto)
                break

        if total_vendido_do_produto > 0:
            print(f"Total vendido do produto '{produto_procurado}': {total_vendido_do_produto}")
        

    elif opcao == 3:
        if lista_produtos:
            mais_vendido = produto_mais_vendido(lista_produtos)
            print(f"O produto mais vendido foi '{mais_vendido[1]}' com {mais_vendido[0]} unidades vendidas.")
        
    elif opcao == 4:
        if lista_produtos:
            print(f"O valor total de vendas é {total_venda(lista_produtos)}")
        
    elif opcao == 5:
        print("Saindo do programa...")
        sair = False

    else:
        print("Opção inválida! Tente novamente.")
