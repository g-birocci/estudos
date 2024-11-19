lista_produtos = []

def total_venda(lista_produtos):

    resultado = produto["preco"] * produto["quantidade_vendida"]
    return resultado


def produto_mais_vendido():
    

while sair:

    produto ={}
    print("1-- Cadatrar produto: ")
    print("2-- Total de vendas. ")
    print("3 -- Produto mais vendido: ")
    print("4-- Total de vendas: ")
    print("5-- Sair")

    opsion = int(input("Digite o numero da opção desejada: "))

    if opsion == 1:
        nome = input("Nome do Produto: ").lower()
        preco = int(input("Digite o Preço do Produto: "))
        quantidade_vendida = int(input("Quantidade total de produto vendido: "))

    produto.update({
        "nome" : nome,
        "preco" : preco,
        "quantidade_vendida" : quantidade_vendida, 
    })

    lista_produtos.append(produto)

    if opsion == 2:
        produto_procurado = input("Qual produto deseja calcular; ")
        total_vendido_do_produto = 0
        
        for produto in lista_produtos:
            if produto_procurado == produto["nome"]:
                total_vendido_do_produto = total_venda(produto)
        print(total_vendido_do_produto)
                
    if opsion == 5:
        sair = False

print("O programa terminou!")
