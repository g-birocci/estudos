class Funcionario:
    def __init__(self, nome, salario, departamento):
        self.nome = nome
        self.salario = salario
        self.departamento = departamento

    def exibir_dados(self):
        print("Nome:", self.nome)
        print("Salário:", self.salario)
        print("Departamento: ", self.departamento)
        