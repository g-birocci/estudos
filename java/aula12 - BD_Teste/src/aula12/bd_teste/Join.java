package aula12.bd_teste;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.ResultSet;

public class Join {
    public static void joifun(Connection con) {
        if (con == null) {
            System.err.println("Conexão inválida! Verifique o banco de dados.");
            return;
        }

        String query = "SELECT funcionario.ID_Funcionario, funcionario.Nome, departamento.nome_DPT " +
                       "FROM funcionario " +
                       "JOIN departamento ON funcionario.ID_Departamento = departamento.ID_Departamento";

        try (Statement stmt = con.createStatement();
             ResultSet rs = stmt.executeQuery(query)) {

            System.out.println("ID_Funcionario | Nome | Nome_Departamento");
            System.out.println("--------------------------------------");
            while (rs.next()) {
                int idFunc = rs.getInt("ID_Funcionario");
                String nomeFunc = rs.getString("Nome");
                String nomeDepto = rs.getString("nome_DPT"); // Nome correto da coluna
                System.out.println(idFunc + " | " + nomeFunc + " | " + nomeDepto);
            }
        } catch (SQLException e) {
            System.err.println("Erro ao executar a consulta: " + e.getMessage());
        }
    }
}
