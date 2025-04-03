/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula13;
import java.util.Scanner;

/**
 *
 * @author gabri
 */

public class Aula13 {

    public static void main(String[] args) {
        // Cria um objeto Scanner para ler a entrada do teclado
        Scanner scanner = new Scanner(System.in);

        // Declaração dos arrays
        String[] produtos = new String[5]; // Array para armazenar os nomes dos produtos
        double[] precos = new double[5];  // Array para armazenar os preços dos produtos

        // Loop para solicitar ao usuário que insira os nomes dos produtos
        System.out.println("Por favor, insira os nomes dos produtos:");
        for (int i = 0; i < produtos.length; i++) {
            System.out.print("Digite o nome do produto " + (i + 1) + ": ");
            produtos[i] = scanner.nextLine();
        }

        // Loop para solicitar ao usuário que insira os preços dos produtos
        System.out.println("\nPor favor, insira os preços dos produtos:");
        for (int i = 0; i < precos.length; i++) {
            System.out.print("Digite o preço do produto " + produtos[i] + ": ");
            while (!scanner.hasNextDouble()) { // Verifica se a entrada é um número válido
                System.out.println("Entrada inválida! Por favor, digite um número.");
                System.out.print("Digite o preço do produto " + produtos[i] + ": ");
                scanner.next(); // Limpa a entrada inválida
            }
            double preco = scanner.nextDouble();
            while (preco < 0) { // Validação para preços negativos
                System.out.println("Preço inválido! O preço deve ser um valor positivo.");
                System.out.print("Digite o preço do produto " + produtos[i] + ": ");
                while (!scanner.hasNextDouble()) {
                    System.out.println("Entrada inválida! Por favor, digite um número.");
                    System.out.print("Digite o preço do produto " + produtos[i] + ": ");
                    scanner.next(); // Limpa a entrada inválida
                }
                preco = scanner.nextDouble();
            }
            precos[i] = preco;
            scanner.nextLine(); // Limpa o buffer do Scanner após a leitura do número
        }

        // Impressão dos produtos e preços no formato solicitado
        System.out.println("\nProduto\tPreço");
        for (int i = 0; i < produtos.length; i++) {
            System.out.printf("%s\tR$ %.2f%n", produtos[i], precos[i]);
        }

        // Fecha o Scanner para liberar recursos
        scanner.close();
    }
}