from usuario import Usuario

class Aluno(Usuario):
    def __init__(self, nome, email, curso = None):
        super().__init__(nome, email)
        self.curso = curso if curso is not None else []
    

    def exibir_info(self):
        super().exibir_info()
        print("Curso: ", self.curso)
        
    def add_aluno(self, aluno):
        self.curso.append(aluno)
        print(f"Aluno {aluno} adicionado ao curso com sucesso!")

          
