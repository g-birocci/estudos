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
public class insert {
    public static void insertFuncionario(Connection con) {
        if (con == null) {
            System.err.println("Conexão inválida! Verifique o banco de dados.");
            return;
        }

        Scanner scanner = new Scanner(System.in);

        System.out.println("Digite o ID do Funcionário:");
        int idFuncionario = scanner.nextInt();
        scanner.nextLine(); // Consumir quebra de linha

        System.out.println("Digite o nome do Funcionário:");
        String nome = scanner.nextLine();

        System.out.println("Digite a morada:");
        String morada = scanner.nextLine();

        System.out.println("Digite o telefone:");
        String telefone = scanner.nextLine();

        System.out.println("Digite o email:");
        String email = scanner.nextLine();

        System.out.println("Digite o ID do Departamento:");
        int idDpt = scanner.nextInt();

        System.out.println("Digite o ID da Função:");
        int idFuncao = scanner.nextInt();

        String query = "INSERT INTO funcionario (ID_Funcionario, Nome, Morada, Telefone, Email, ID_DPT, ID_Funcao) " +
                       "VALUES (?, ?, ?, ?, ?, ?, ?)";

        try (PreparedStatement pstmt = con.prepareStatement(query)) {
            pstmt.setInt(1, idFuncionario);
            pstmt.setString(2, nome);
            pstmt.setString(3, morada);
            pstmt.setString(4, telefone);
            pstmt.setString(5, email);
            pstmt.setInt(6, idDpt);
            pstmt.setInt(7, idFuncao);

            int linhasAfetadas = pstmt.executeUpdate();
            if (linhasAfetadas > 0) {
                System.out.println("Funcionário inserido com sucesso!");
            } else {
                System.out.println("Erro ao inserir funcionário.");
            }
        } catch (SQLException e) {
            System.err.println("Erro ao inserir funcionário: " + e.getMessage());
        }
    }
}