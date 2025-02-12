from pessoa import Funcionario
from departamento import Funcionario_pessoa

#funcionario = Funcionario("Gabriel", 5000)
#funcionario.exibir_dados()

funcionario = Funcionario("Gabriel", 2000, "Programador\n")
programador = Funcionario_pessoa("Gabriel", 3000, "TI", "C#\n")

funcionario.exibir_dados()

programador.programador()
