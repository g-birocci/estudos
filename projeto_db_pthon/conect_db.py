import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",  # usuário
    password="123456",  #senha do MySQL
    database="aluno"
)

cursor = conexao.cursor()


cursor.execute.cursor("SELECT * FROM alunos")

for linha in cursor.fetchall():
    print(linha)

cursor.close()
conexao.close()