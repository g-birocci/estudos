package aula12.bd_teste;

import java.sql.Connection;
import java.sql.SQLException;
import java.sql.Statement;
import java.sql.ResultSet;

public class Select {
    public static void selfun(Connection con) {
        if (con == null) {
            System.err.println("Conexão inválida! Verifique o banco de dados.");
            return;
        }

        String query = "SELECT " +
            "    funcionario.ID_Funcionario AS id_funcionario, " +
            "    funcionario.Nome AS nome_funcionario, " +
            "    departamento.ID_DPT AS id_departamento, " +
            "    departamento.Nome_DPT AS nome_departamento " +
            "FROM funcionario " +
            "INNER JOIN departamento ON funcionario.ID_DPT = departamento.ID_DPT";

        try (Statement stmt = con.createStatement();
             ResultSet rs = stmt.executeQuery(query)) {

            System.out.println("ID_Funcionario | Nome | ID_Departamento | Nome_Departamento");
            System.out.println("------------------------------------------------------------");

            while (rs.next()) {
                int idFunc = rs.getInt("id_funcionario");  // Pegando pelo alias
                String nomeFunc = rs.getString("nome_funcionario"); // Pegando pelo alias
                int idDept = rs.getInt("id_departamento");  // Pegando pelo alias
                String nomeDept = rs.getString("nome_departamento");  // Pegando pelo alias

                System.out.println(idFunc + " | " + nomeFunc + " | " + idDept + " | " + nomeDept);
            }

        } catch (SQLException e) {
            System.err.println("Erro ao executar a consulta: " + e.getMessage());
        }
    }
}