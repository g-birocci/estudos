from usuario import Usuario

class Instrutor(Usuario):
    def __init__(self, nome, email, cursos_ministrados=None):
        super().__init__(nome, email)
        self.cursos_ministrados = cursos_ministrados if cursos_ministrados is not None else []

    def exibir_info(self):
        pai_info = super().exibir_info()
        cursos = ', '.join(self.cursos_ministrados) if self.cursos_ministrados else "Nenhum"
        return f"{pai_info}\nCursos Ministrados: {cursos}"

    def to_dict(self):
        data = super().to_dict()
        data.update({
            'tipo': 'instrutor',
            'cursos_ministrados': self.cursos_ministrados
        })
        return data