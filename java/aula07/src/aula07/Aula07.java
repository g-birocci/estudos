/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula07;
import java.util.Scanner;
/**
 *
 * @author gabri
 */
public class Aula07 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        while(true) {
            System.out.println("Digite um numero pra ver se ele é impar ou par: ");
            int num = scanner.nextInt();
        
            if (num == 0)
                break;
                
            String resp = (num % 2 == 0) ? "Par" : "Ìmpar";
            System.out.println("O numero " + num + " é " + resp);
            
            }
        scanner.close();
    }
}
