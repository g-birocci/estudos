import mysql.connector
from mysql.connector import Error

def verificar_conexao():
    try:
        # Substitua pelos detalhes do seu servidor
        conexao = mysql.connector.connect(
            host="10.100.30.149",        # Endereço do servidor (use o IP ou domínio se não for local)
            user="root",             # Usuário do banco de dados
            password="123456",    # Senha do banco de dados
            database="alunos", # Nome do banco de dados (opcional)
            unix_socket="/run/mysqld/mysqld.sock"
        )

        if conexao.is_connected():
            print("Conexão bem-sucedida ao servidor MySQL!")
            print(f"Servidor: {conexao.server_host}")
            print(f"Versão: {conexao.get_server_info()}")
    except Error as e:
        print("Erro ao conectar ao servidor MySQL:", e)
    finally:
        if 'conexao' in locals() and conexao.is_connected():
            conexao.close()
            print("Conexão encerrada.")


# Chamar a função
verificar_conexao()

