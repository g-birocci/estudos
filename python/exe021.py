lista = []

while True:
    print("\nVocê está no menu, escolha uma opção abaixo:")
    print("1 -- Adicionar um contato")
    print("2 -- Remover um contato")
    print("3 -- Visualizar um contato")
    print("4 -- Buscar contato por tag (conhece de onde ou apelido)")
    print("5 -- Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Qual é o nome do contato? ")
        telefone = input("Qual é o telefone do contato? ")
        email = input("Qual é o email do contato? ")
        tag1 = input("Você o conhece de onde? ")
        tag2 = input("Qual é o apelido? ")

        contatos = {
            "nome": nome,
            "telefone": telefone,
            "email": email,
            "tags": {tag1, tag2}
        }
        lista.append(contatos)
        print(f"Contato de {nome} adicionado com sucesso!")

    elif opcao == "2":
        nome = input("Digite o nome do contato que quer remover: ")
        encontrado = False
        for dicio in lista:
            if nome == dicio["nome"]:
                lista.remove(dicio)
                print(f"O contato {nome} foi removido com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print(f"O contato {nome} não foi encontrado.")

    elif opcao == "3":
        nome = input("Qual é o nome do contato que deseja visualizar? ")
        encontrado = False
        for dicio in lista:
            if nome == dicio["nome"]:
                print(f"\nNome: {dicio['nome']}")
                print(f"Telefone: {dicio['telefone']}")
                print(f"Email: {dicio['email']}")
                print(f"Tags: {', '.join(dicio['tags'])}")
                encontrado = True
                break
        if not encontrado:
            print(f"O contato {nome} não foi encontrado.")

    elif opcao == "4":
        tag_procurada = input("Digite a tag para buscar contatos: ")
        encontrados = False
        for contato in lista:
            if tag_procurada in contato["tags"]:
                print(f"\nNome: {contato['nome']}")
                print(f"Telefone: {contato['telefone']}")
                print(f"Email: {contato['email']}")
                print(f"Tags: {', '.join(contato['tags'])}")
                encontrados = True
        if not encontrados:
            print("Nenhum contato encontrado com essa tag.")

    elif opcao == "5":
        print("Saindo do programa!")
        break

    else:
        print("Opção inválida, tente novamente!")
