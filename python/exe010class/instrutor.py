from usuario import Usuario

class Instrutor(Usuario):
    def __init__(self, nome, email, curso_ministrado = None ):
        super().__init__(nome, email)
        self.curso_ministrado = curso_ministrado if curso_ministrado is not None else []

    def exibir_info(self):
        super().exibir_info()
        print("Formador: ", self.curso_ministrado)

    def add_instrutor(self, instrutor):
        self.curso_ministrado.append(instrutor)
        print(f"Instrutor {instrutor} adicionado com sucesso!")

    