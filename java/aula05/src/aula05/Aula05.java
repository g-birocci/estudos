/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula05;
import java.util.Scanner;

/**
 *
 * @author gabri
 */
public class Aula05 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("-- Calculando a média --");
        System.out.println("Digite o primeiro numero: ");
        double n = scanner.nextDouble();
        System.out.println("Digite o segundo numero: ");
        double n2 = scanner.nextDouble();
        System.out.println("Digite o ultimo numero: ");
        double n3 = scanner.nextDouble();
        
        double media = (n + n2 + n3) / 3;
        
        System.out.println("A média dos numero é " + media);
        
        scanner.close();
        
        
        
    }
    
}
