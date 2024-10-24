liista = []
contacto={}

while True:
   
    print("Bem Vindo")
    nome = input("Digite o seu nome: ")
    telefone = int(input("Digite o telefone: "))
    email = 
    n_tags = int(input("quantas tags?"))
    tags = []
    for n in range(0,n_tags):
        tag = input("Insira a tag: amigo, trabalho ou familia")
        tags.append(tag)
    set_tags = set(tags)

    contacto.update({"nome": nome, "telefone": telefone, "email": email, "tags": set_tags})
    liista.append(contacto)

    print(liista)