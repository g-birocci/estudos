/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula10;
import java.util.Scanner;

/**
 *
 * @author gabri
 */
public class Aula10 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String[] nomes; //declara o vetor
        nomes = new String[5]; //Declaro o tamanho do vetor
        
        for (int i = 0; i < nomes.length; i++) {
            System.out.println("Digite o " + i + "ª nome: ");
            nomes[i] = scanner.nextLine();
        }
        
        System.out.println("\nNomes cadastrados:");
        
        for (String nome : nomes ) {
            System.out.println(nome);
        }
        scanner.close();
    }
}
