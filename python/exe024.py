liista = []
sair = True

while sair:
    print("Bem-vindo de volta")
    
    contacto = {}
    
    nome = input("Digite o nome do contato: ").lower()
    telefone = int(input("Digite o telefone: "))
    email = input("Digite o email: ").lower()
    
    n_tags = int(input("Quantas tags? "))
    tags = [input("Insira a tag: ") for _ in range(n_tags)]
    set_tags = set(tags)
    
    contacto.update({"nome": nome, "telefone": telefone, "email": email, "tags": set_tags})
    liista.append(contacto)

    find = input("Deseja pesquisar um contato por nome[1], tag[2] ou continuar[3]?  ").strip()
    if find == "1":
        opname = input("Digite o nome: ").lower()
        encontrado = False
        for procurado in liista:
            if procurado["nome"] == opname:
                print("Contato encontrado:", procurado)
                encontrado = True
                sair = False
        if not encontrado:
            print("contato não encontrado.")
                
    elif find == "2":
        tag_procurada = input("Digite a tag: ").lower()
        encontrado = False
        for procurado in liista:
            if tag_procurada in procurado["tags"]:
                print("Contato encontrado:", procurado)
                encontrado = True
                sair = False
        if not encontrado:
            print("tag não encontrada.")
            sair = False
    elif find == "3":
        sair = True
print("Fim do programa")    
print("Lista de contatos cadastrados:")
print(liista)
