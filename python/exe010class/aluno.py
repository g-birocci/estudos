from usuario import Usuario

class Aluno(Usuario):
    def __init__(self, nome, email, curso_inscrito = None):
        super().__init__(nome, email)
        self.curso_inscrito = curso_inscrito if curso_inscrito is not None else []
    
    def exibir_info(self):
        pai_info = super().exibir_info()
        curso = ', '.join(self.curso_inscrito) if self.curso_inscrito is not None else []
        return f"{pai_info}\nCursos Inscritos: {curso}"
        
    def to_dict(self):
        data = super().to_dict()
        data.update({
            'tipo': 'aluno',
            'cursos_inscritos': self.curso_inscrito
        })
        return data
          
