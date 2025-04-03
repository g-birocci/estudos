/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aula12.bd_teste;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.Scanner;

/**
 *
 * @author gabri
 */

public class deletar {
    public static void deleteFuncionario(Connection con) {
        if (con == null) {
            System.err.println("Conexão inválida! Verifique o banco de dados.");
            return;
        }

        // Listar funcionários antes da deleção
        Select.selfun(con);

        Scanner scanner = new Scanner(System.in);
        System.out.println("Digite o ID do funcionário que deseja deletar: ");

        if (!scanner.hasNextInt()) {
            System.out.println("Erro: Você não digitou um número válido!");
            return;
        }

        int idFuncionario = scanner.nextInt();
        scanner.nextLine(); // Consumir quebra de linha

        // Validar ID positivo
        if (idFuncionario <= 0) {
            System.out.println("Erro: O ID deve ser um número positivo.");
            return;
        }

        // Verificar se o ID existe no banco de dados
        String checkQuery = "SELECT COUNT(*) FROM funcionario WHERE ID_Funcionario = ?";
        try (PreparedStatement checkStmt = con.prepareStatement(checkQuery)) {
            checkStmt.setInt(1, idFuncionario);
            try (var rs = checkStmt.executeQuery()) {
                if (rs.next() && rs.getInt(1) == 0) {
                    System.out.println("Nenhum funcionário encontrado com esse ID.");
                    return;
                }
            }
        } catch (SQLException e) {
            System.err.println("Erro ao verificar o ID do funcionário: " + e.getMessage());
            return;
        }

        // Confirmar deleção
        System.out.println("Tem certeza que deseja deletar o funcionário com ID " + idFuncionario + "? (S/N): ");
        String confirmacao = scanner.nextLine().trim().toUpperCase();

        if (!confirmacao.equals("S")) {
            System.out.println("Operação cancelada pelo usuário.");
            return;
        }

        // Deletar o funcionário
        String sql = "DELETE FROM funcionario WHERE ID_Funcionario = ?";
        try (PreparedStatement stmt = con.prepareStatement(sql)) {
            stmt.setInt(1, idFuncionario);
            int rowsAffected = stmt.executeUpdate();

            if (rowsAffected > 0) {
                System.out.println("Funcionário deletado com sucesso!");
            } else {
                System.out.println("Erro ao deletar funcionário.");
            }
        } catch (SQLException e) {
            System.err.println("Erro ao deletar funcionário: " + e.getMessage());
        }
    }
}