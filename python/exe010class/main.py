from usuario import Usuario
from aluno import Aluno

cursos_disponiveis = {
    1: "TI",
    2: "Programador",
    3: "Web Developer",
    4: "Front End",
    5: "Back End",
}

alunos = []

while True:

    aluno_nome = str(input("Digite o nome do aluno: "))
    aluno_email = str(input("Digite o email do aluno: "))
    
    print("""Escolha o curso do aluno:
          1 -- TI
          2 -- Programador
          3 -- Web developer
          4 -- Front end
          5 -- Back end """)
    
    op = int(input(("Digite o numero da opção desejada: ")))

    if op in cursos_disponiveis:
        cursos_disponiveis = cursos_disponiveis[op]
    else:
        print("Opção inválida. Tente novamente")

    

    aluno = Aluno(aluno_nome, aluno_email)
    aluno.add_aluno(aluno)

    alunos.append(aluno)

    continuar = input("Deseja adicionar outro aluno? (s/n): ").lower()
    if continuar != 's':
        break






