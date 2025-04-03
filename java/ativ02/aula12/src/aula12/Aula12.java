/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula12;
import java.util.Scanner;

/**
 *
 * @author gabri
 */
public class Aula12 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Cria um objeto Scanner para ler a entrada do teclado
        Scanner scanner = new Scanner(System.in);

        // Declara um array de double com 5 posições para armazenar os preços
        double[] precos = new double[5];

        
        for (int i = 0; i < precos.length; i++) {
            System.out.print("Digite o preço do produto " + (i + 1) + ": ");
            while (!scanner.hasNextDouble()) { 
                System.out.println("Entrada inválida! Por favor, digite um número.");
                System.out.print("Digite o preço do produto " + (i + 1) + ": ");
                scanner.next();
            }
            precos[i] = scanner.nextDouble();
        }


        //
        System.out.println("\nOs preços inseridos foram:");
        for (int i = 0; i < precos.length; i++) {
            System.out.printf("Produto %d - £ %.2f%n", (i + 1), precos[i]);
        }

        // Fecha o Scanner para liberar recursos
        scanner.close();
    }
    
}
