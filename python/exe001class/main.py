from biblioteca import Biblioteca
from livro import Livro

# Criando a biblioteca e alguns livros
obj_biblioteca = Biblioteca("Gaia", "Av República 345")

print("Bem-vindo à Livraria!")
print("-" * 60)

while True:
    print("\nSelecione o que você deseja fazer:")
    print('''
        1 -- Adicionar um livro
        2 -- Remover um livro
        3 -- Buscar um livro
        4 -- Exibir os livros
        5 -- Sair
    ''')

    op = input("Digite a opção desejada: ").strip()

    match op:
        case "1":  # Adicionar livro
            while True:
                nome = input("Digite o nome do livro: ").strip()
                if nome:
                    break
                print("Erro: O nome do livro não pode ser vazio. Tente novamente.")

            while True:
                autor = input("Digite o nome do autor: ").strip()
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
            obj_biblioteca.adicionar_livro(obj_livro)  # Adiciona o livro à biblioteca
            print(f"Livro '{obj_livro.titulo}' adicionado com sucesso!")

        case "2":  # Remover livro
            while True:
                titulo = input("Digite o título do livro para remover: ").strip()
                if titulo:
                    break
                print("Erro: O título não pode ser vazio. Tente novamente.")

            removido = obj_biblioteca.remover_livro(titulo)

            if removido:
                print(f"O livro '{titulo}' foi removido com sucesso.")
            else:
                print(f"Erro: O livro '{titulo}' não foi encontrado.")

        case "3":  # Buscar livro
            titulo = input("Digite o título do livro que deseja buscar: ").strip()
            livro_encontrado = obj_biblioteca.buscar_livro(titulo)

            if livro_encontrado:
                print(f"Livro encontrado: {livro_encontrado}")
            else:
                print(f"Erro: O livro '{titulo}' não foi encontrado.")

        case "4":  # Exibir livros
            if obj_biblioteca.lista_dos_livros:
                print("\nLista de livros disponíveis:")
                for livro in obj_biblioteca.lista_dos_livros:
                    print(livro)  # Certifique-se de implementar __str__ na classe Livro
            else:
                print("Nenhum livro disponível na biblioteca.")

        case "5":  # Sair
            print("Saindo da livraria. Até logo!")
            break

        case _:  # Opção inválida
            print("Opção inválida! Tente novamente.")
