package projeto.database;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class ConexaoBD {
    // Configurações do banco de dados
    private static final String URL = "jdbc:mysql://localhost:3306/contatos_java";
    private static final String USER = "root";
    private static final String PASSWORD = "";
    private static Connection conexao = null;

    public static Connection conectar() {
        if (conexao == null || estaFechada(conexao)) {
            try {
                // Registrar o driver JDBC
                Class.forName("com.mysql.cj.jdbc.Driver");
                
                // Tentar estabelecer a conexão
                conexao = DriverManager.getConnection(URL, USER, PASSWORD);
                
                if (conexao != null) {
                    System.out.println("Conexão estabelecida com sucesso!");
                }
                
            } catch (ClassNotFoundException e) {
                System.err.println("Driver MySQL não encontrado: " + e.getMessage());
            } catch (SQLException e) {
                if (e.getErrorCode() == 1049) { // Database doesn't exist
                    try {
                        // Conectar sem especificar o banco de dados
                        Connection tempConn = DriverManager.getConnection(
                            "jdbc:mysql://localhost:3306/",
                            USER,
                            PASSWORD
                        );
                        
                        // Criar o banco de dados
                        tempConn.createStatement().executeUpdate(
                            "CREATE DATABASE IF NOT EXISTS contatos_java"
                        );
                        
                        // Fechar conexão temporária
                        tempConn.close();
                        
                        // Tentar conectar novamente com o banco criado
                        conexao = DriverManager.getConnection(URL, USER, PASSWORD);
                        
                        // Criar a tabela se não existir
                        String createTable = """
                            CREATE TABLE IF NOT EXISTS contatos (
                                id BIGINT PRIMARY KEY AUTO_INCREMENT,
                                nome VARCHAR(100) NOT NULL,
                                telefone VARCHAR(20),
                                email VARCHAR(100)
                            )
                        """;
                        conexao.createStatement().executeUpdate(createTable);
                        
                    } catch (SQLException ex) {
                        System.err.println("Erro ao criar banco de dados: " + ex.getMessage());
                    }
                } else {
                    System.err.println("Erro ao conectar ao banco de dados: " + e.getMessage());
                }
            }
        }
        return conexao;
    }

    private static boolean estaFechada(Connection conn) {
        try {
            return conn == null || conn.isClosed();
        } catch (SQLException e) {
            return true;
        }
    }
} 