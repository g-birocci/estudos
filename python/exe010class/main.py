from aluno import Aluno
from instrutor import Instrutor
from base_sistema import Base
base = Base()

try:
    base.carregar_usuarios('usuarios.json')
    print("Dados carregados com sucesso!")
except FileNotFoundError:
    print("Nenhum dados anterior encontrado. Iniciando com uma lista vazia.")


while True:
    print('''
        1 -- Adicionar aluno
        2 -- Adicionar instrutor
        3 -- Listar alunos
        4 -- Listar instrutores
        5 -- Sair
    ''')

    opc = input("Escolha a opção desejada: ")

    match opc:
        case "1":
            aluno_nome = input("Digite o nome do aluno: ")
            aluno_email = input("Digite o email do aluno: ")

            print("""Escolha o curso do aluno:
                1 -- TI
                2 -- Programador
                3 -- Web Developer
                4 -- Front End
                5 -- Back End""")

            op = int(input("Digite o número da opção desejada: "))

            if op in base.cursos_disponiveis:
                curso = base.cursos_disponiveis[op]
            else:
                print("Opção inválida. Tente novamente.")
                continue

            aluno = Aluno(aluno_nome, aluno_email, [curso])
            base.add_aluno(aluno)
            base.salvar_usuarios('usuarios.json')
            print("Aluno adicionado com sucesso!")

        case "2":
            instrutor_nome = input("Digite o nome do instrutor: ")
            instrutor_email = input("Digite o email do instrutor: ")

            print("""Escolha o curso ministrado pelo instrutor:
                1 -- TI
                2 -- Programador
                3 -- Web Developer
                4 -- Front End
                5 -- Back End""")

            op = int(input("Digite o número da opção desejada: "))

            if op in base.cursos_disponiveis:
                curso = base.cursos_disponiveis[op]
            else:
                print("Opção inválida. Tente novamente.")
                continue

            instrutor = Instrutor(instrutor_nome, instrutor_email, [curso])
            base.add_instrutor(instrutor)
            base.salvar_usuarios('usuarios.json')
            print("Instrutor adicionado com sucesso!")

        case "3":
            base.listar_alunos()

        case "4":
            base.listar_instrutores()

        case "5":
            break

        case _:
            print("Opção inválida.")