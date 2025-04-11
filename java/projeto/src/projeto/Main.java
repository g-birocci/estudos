package projeto;

import java.sql.Connection;

public class Main {
    public static void main(String[] args) {
        // Testar a conexão com o banco de dados
        Connection conexao = ConexaoBD.conectar();

        if (conexao == null) {
            System.err.println("Erro ao conectar com o banco de dados. O programa será encerrado.");
            return;
        }

        System.out.println("Conexão validada! Prosseguindo com as operações...");

        listarContatos(conexao);

        try {
            if (conexao != null) {
                conexao.close();
                System.out.println("Conexão encerrada com sucesso.");
            }
        } catch (Exception e) {
            System.err.println("Erro ao encerrar a conexão: " + e.getMessage());
        }
    }

    private static void listarContatos(Connection conexao) {
        String sql = "SELECT * FROM contatos";
        try (var stmt = conexao.createStatement(); var rs = stmt.executeQuery(sql)) {
            System.out.println("ID | Nome | Telefone | Email");
            System.out.println("------------------------------");

            while (rs.next()) {
                int id = rs.getInt("id");
                String nome = rs.getString("nome");
                String telefone = rs.getString("telefone");
                String email = rs.getString("email");
                System.out.printf("%d | %s | %s | %s%n", id, nome, telefone, email);
            }
        } catch (Exception e) {
            System.err.println("Erro ao listar contatos: " + e.getMessage());
        }
    }
}
