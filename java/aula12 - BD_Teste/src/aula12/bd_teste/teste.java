/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula12.bd_teste;
import java.sql.Connection;
import java.util.Scanner;

public class teste {
    public static void main(String[] args) {
        Connection con = cnDB.conectar();
        Scanner scanner = new Scanner(System.in);

        try {
            
            while (true) {
                System.out.println("-- Menu Principal --");
                System.out.println("1. Adicionar funcionário.");
                System.out.println("2. Listar funcionários.");
                System.out.println("3. Deletar um funcionário.");
                System.out.println("4. Alterar funcionário.");
                System.out.println("5. Sair");
                System.out.println("Escolha uma opção: ");

                int op = scanner.nextInt();

                switch (op) {
                    case 1:
                        insert.insertFuncionario(con);
                        break;
                    case 2:
                        Select.selfun(con);
                        break;
                    case 3:
                        deletar.deleteFuncionario(con);
                        break;
                    case 4:
                        alterar.updateFuncionario(con);
                        break;
                    case 5:
                        System.out.println("Saindo do programa...");
                        return;
                    default:
                        System.out.println("Opção inválida.");
                }
            }
        } catch (Exception e) {
            System.err.println("Erro inesperado: " + e.getMessage());
        } finally {
            if (con != null) {
                try {
                    con.close();
                } catch (Exception e) {
                    System.err.println("Erro ao fechar conexão: " + e.getMessage());
                }
            }
            scanner.close();
        }
    }
}