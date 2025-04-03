/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula11;
import java.util.Scanner;

/**
 *
 * @author gabri
 */
public class Aula11 {

    /**
     * @param args the command line arguments
     */
      public static void main(String[] args) {
        // Cria um objeto Scanner para ler a entrada do teclado
        Scanner scanner = new Scanner(System.in);

        // Declara um array de Strings com 5 posições
        String[] produtos = new String[5];


        // Loop para solicitar ao usuário que insira os nomes dos produtos
        for (int i = 0; i < produtos.length; i++) {
            System.out.print("Digite o nome do produto " + (i + 1) + ": ");
            produtos[i] = scanner.nextLine();
        }

        // Exibe os produtos inseridos pelo usuário
        System.out.println("\nOs produtos inseridos foram:");
        for (int i = 0; i < produtos.length; i++) {
            System.out.println((i + 1) + " - " + produtos[i]);
        }

        // Fecha o Scanner para liberar recursos
        scanner.close();
    }
    
}
