/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Class.java to edit this template
 */
package aula12.bd_teste;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.SQLException;
import java.util.InputMismatchException;
import java.util.Scanner;

/**
 *
 * @author gabri
 */
public class alterar {
    public static void updateFuncionario(Connection con) {
        if (con == null) {
            System.err.println("Conexão inválida! Verifique o banco de dados.");
            return;
        }

        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("Digite o ID do Funcionário a ser atualizado:");
            int idFuncionario = scanner.nextInt();
            scanner.nextLine(); 

            System.out.println("Digite o novo nome do Funcionário:");
            String nome = scanner.nextLine();

            System.out.println("Digite a nova morada:");
            String morada = scanner.nextLine();

            System.out.println("Digite o novo telefone:");
            String telefone = scanner.nextLine();

            System.out.println("Digite o novo email:");
            String email = scanner.nextLine();

            System.out.println("Digite o novo ID do Departamento:");
            int idDpt = scanner.nextInt();

            System.out.println("Digite o novo ID da Função:");
            int idFuncao = scanner.nextInt();

            String query = "UPDATE funcionario SET Nome = ?, Morada = ?, Telefone = ?, Email = ?, ID_DPT = ?, ID_Funcao = ? " +
                           "WHERE ID_Funcionario = ?";

            try (PreparedStatement pstmt = con.prepareStatement(query)) {
                pstmt.setString(1, nome);
                pstmt.setString(2, morada);
                pstmt.setString(3, telefone);
                pstmt.setString(4, email);
                pstmt.setInt(5, idDpt);
                pstmt.setInt(6, idFuncao);
                pstmt.setInt(7, idFuncionario);

                int linhasAfetadas = pstmt.executeUpdate();
                if (linhasAfetadas > 0) {
                    System.out.println("Funcionário atualizado com sucesso!");
                } else {
                    System.out.println("Nenhum funcionário encontrado com esse ID.");
                }
            } catch (SQLException e) {
                System.err.println("Erro ao atualizar funcionário: " + e.getMessage());
                e.printStackTrace(); // Para depuração
            }
        } catch (InputMismatchException e) {
            System.err.println("Erro: Entrada inválida. Certifique-se de inserir valores corretos.");
        } finally {
            scanner.close();
        }
    }
}