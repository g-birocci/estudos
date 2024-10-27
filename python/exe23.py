liista = []
contacto={}
sair = True
while sair == True:
   
    print("Bem Vindo")
    nome = input("Digite o seu nome: ")
    telefone = int(input("Digite o telefone: "))
    email = input("Digite o seu email: ")
    n_tags = int(input("Quantas tags? "))
    tags = []
    for n in range(0,n_tags):
        tag = input("Insira a tag: ")
        tags.append(tag)
    set_tags = set(tags)

    contacto.update({"nome": nome, "telefone": telefone, "email": email, "tags": set_tags})
    liista.append(contacto)

    find = input("Deseja Pesquisar um contato ? [S/N]").lower()
    if find == "s":
        op = input("Deseja pesquisar por [nome] ou [tag] ?").lower()
        op == "nome"
        opname = input("Digite o nome: ")
        for procurado in liista: 
            if contacto["nome"] == opname:
                print(contacto)
            else:
                print("Pessoa não encontrada")
    
    else:
        sair = input("Deseja Continuar [S/N] ")
        if sair == "N":
            sair = False
        else:
            sair = True
print(liista)
    