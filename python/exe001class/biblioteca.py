class Biblioteca():
    def __init__(self, nome, endereco):
        self.lista_dos_livros = []
        self.nome = nome
        self.endereco = endereco
        
    def adcionar_livro(self, obj_livro):
        self.lista_dos_livros.append(obj_livro)
      #fazer o return e remover o print e ajustar no main  
    def remover_livro(self, titulo):
        for livro in self.lista_dos_livros:
            if livro.titulo == titulo:
                self.lista_dos_livros.remove(livro)  
                return True
            else:
                return False
        
    def buscar_livro(self,titulo):
        for livro in self.lista_dos_livros:
            if livro.titulo == titulo:
                return livro
            else:
                return None
