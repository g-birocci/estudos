class Biblioteca():
    def __init__(self, nome, endereco):
        self.lista_dos_livros = []
        self.nome = nome
        self.endereco = endereco
    
    def adicionar_livro(self, obj_livro):
        self.lista_dos_livros.append(obj_livro)
        return True
    
    def remover_livro(self, titulo):
        for livro in self.lista_dos_livros:
            if livro.titulo == titulo:
                self.lista_dos_livros.remove(livro)
                return True
        return False  # Não encontrado
    
    def buscar_livro(self, titulo):
        for livro in self.lista_dos_livros:
            if livro.titulo == titulo:
                return livro
        return None  # Não encontrado
