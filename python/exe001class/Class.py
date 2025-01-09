class Livro():
    def __init__(self, titulo, autor, ano):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano

    def mostra_livro(nome_livro):
        print("Ola")


class Biblioteca():
    def __init__(self, nome, endereco, livros):
        self.lista_dos_livro = []
        self. nome = nome
        self.endereco = endereco
        self.livros = livros
        
    def adcionanar_livro(self, titulo, autor, ano):
        livro = {"titulo": titulo, "autor": autor, "ano": ano}
        self.lista_dos_livro.append(livro)
        print(f"O livro {titulo} foi adicionado a biblioteca.")

    def remover_livro():
        print("")
        