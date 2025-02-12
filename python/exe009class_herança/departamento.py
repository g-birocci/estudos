from pessoa import Funcionario

class Funcionario_pessoa(Funcionario):

    def __init__(self, nome, salario, departamento, linguagen):
        super().__init__(nome, salario, departamento)
        self.linguagen = linguagen
        

    def programador(self):
        super().exibir_dados()
        print("Linguagen", self.linguagen)
        


