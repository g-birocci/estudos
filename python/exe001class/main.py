from biblioteca import Biblioteca
from livro import Livro


obj_biblioteca = Biblioteca("gaia", "Av republica 345")
obj_livro_python = Livro("python", "carlos", 2025)
obj_livro_php = Livro("php", "alex", 1999)

print("Bem- vindo")
print("-*-" * 30)

sair = True
while sair: 
    print("Bem-vindo a Livraria")
    print('''Selecione o que vc deseja fazer
            1 -- Adicionar um livro
            2 -- Remover um livro
            3 -- Buscar um livro
            4 -- Exibir os livros
            5 -- Sair
        ''')
    op = str(input(("Digite a opcão desejada: ")))

    match op:

        case "1":

            while True: 
                nome = input("Digite o nome do livro: ").strip().upper()
                if nome:
                    break
                print("Erro: O nome do livro não pode ser vazio. Tente novamente.")

            while True:
                autor = input("Digite o nome do autor: ").strip().upper()
                if autor:
                    break
                print("Erro: O nome do autor não pode ser vazio. Tente novamente.")

            while True:
                try:
                    ano = int(input("Digite o ano do livro [xxxx]: ").strip())
                    if ano > 0:
                        break
                    print("Erro: O ano deve ser um número positivo. Tente novamente.")
                except ValueError:
                    print("Erro: O ano deve ser um número válido. Tente novamente.")

            # Criação do objeto livro
            obj_livro = Livro(nome, autor, ano)
            obj_biblioteca.adcionar_livro(obj_livro) # Adiciona o livro à biblioteca
            print(f"Livro '{nome}' adicionado com sucesso!")


        case "2":
            titulo = str(input("Digite o titulo do livro pra remover ele: ")).strip().upper()

            remover = Biblioteca(titulo)
            remover.remover_livro(titulo)
            
            print(f"O livro {titulo} foi removido.")

        case "3":
            titulo = str(input("Digite o titulo do livro que deseja buscar: "))


        case "4":
            print("Todos os livros estão abaixo.")


        case "5":
            sair = False
            print("Saindo da livraria. Até logo!")

        case _:
            print("Opção inválida! Tem novamente.")
