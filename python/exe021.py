alunos = {}
lista = []

while True:

    print("1 -- Cadastrar aluno. ")
    print("2 -- Exibir dados de um aluno. ")
    print("3 -- Atualizar dados de um aluno. ")
    print("4 -- Remover um aluno. ")
    print("5 -- Exibir todos os alunos. ")
    print("6 -- Calcular aluno com a maior media de notas")
    print("7 -- Sair. ")

    opsion = (input("Digite a opcão desejada: ")).lower()

    if opsion == 1:
        nome = input("Digite o nome do aluno; ")
        cidade = input("Cidade do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        print("Digite a nota do aluno: ")
        mat = float(input("Nota matematica: "))
        por = float(input("Nota Portugues: "))
        cie = float(input("Nota ciencias: "))

        media_aluno = (mat + por +cie) / 3

        alunos[nome] = {
            "cidade": cidade,
            "idade": idade,
            "notas": {
                "matematica": mat,
                "portugues": por,
                "ciencias": cie,
                "media": media_aluno
            }
        }
        print(f"Aluno {} cadastrado com sucesso!".format(nome))
   
    #elif opsion == 2:
        input('Digite o nome do aluno: ')

    #elif opsion == 3:
    #elif opsion == 4:
