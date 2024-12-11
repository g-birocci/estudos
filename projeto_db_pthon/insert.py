import mysql.connector
from mysql.connector import Error

def inserir_aluno(nome, curso, email):
    try:
        # Conexão com o banco de dados
        conexao = mysql.connector.connect(
            host="10.100.30.149",        # Endereço do servidor (use o IP ou domínio se não for local)
            user="root",             # Usuário do banco de dados
            password="123456",    # Senha do banco de dados
            database="alunos", # Nome do banco de dados (opcional)
            unix_socket="/run/mysqld/mysqld.sock"
        )

        if conexao.is_connected():
            print("Conectado ao banco de dados!")

            # Criação do cursor
            cursor = conexao.cursor()

            # Query para inserir dados
            query = """
            INSERT INTO alunos (nome, curso, email)
            VALUES (%s, %s, %s);
            """

            # Valores a serem inseridos
            valores = (nome, curso, email)

            # Executa a query
            cursor.execute(query, valores)

            # Confirma a transação
            conexao.commit()

            print("Aluno inserido com sucesso!")
    
    except Error as e:
        print(f"Erro ao inserir dados: {e}")
    
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão com o banco encerrada.")


def ver_aluno():
    try:
        # Conexão com o banco de dados
        conexao = mysql.connector.connect(
            host="10.100.30.149",        # Endereço do servidor (use o IP ou domínio se não for local)
            user="root",             # Usuário do banco de dados
            password="123456",    # Senha do banco de dados
            database="alunos", # Nome do banco de dados (opcional)
            unix_socket="/run/mysqld/mysqld.sock"
        )

        if conexao.is_connected():
            print("Conectado ao banco de dados!")

            cursor = conexao.cursor()

            query = """
            SELECT * FROM alunos;
            """
            cursor.execute(query) #executa a função de cima e pesquisa dentro do branco
            

            alunos = cursor.fetchall() 
            print(alunos)
            
            
    finally:
        if conexao.is_connected():
            cursor.close()
            conexao.close()
            print("Conexão com o banco encerrada.")


def atualizar_aluno():
    print("Em manutenção")

def deletar_aluno():
    print("Em manutenção")


sair = True
while sair:
    print("----Banco de Dados Escola Mariadb----")
    print("Insira a opção desejada")
    print("1--Inserir Aluno")
    print("2--Ver Alunos")
    print("3--Atualizar Aluno")
    print("4--Deletar Aluno")
    print("5--Sair")

    op = input("Digite a opção desejada: ")

    match op:
        case "1":
            nome = input("Digite o nome do aluno: ")
            curso = input("Digite o nome da formação: ")
            email = input("Digite o email do aluno: ")
            inserir_aluno(nome, curso, email)

        case "2":
            ver_aluno()

        case "3":
            atualizar_aluno()

        case "4":
            deletar_aluno()

        case "5":
            sair = False

        case _:
            print("Opção inválida")

print("Saindo do sistema...")
        

