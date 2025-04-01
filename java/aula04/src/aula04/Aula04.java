/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula04;
import java.util.Scanner;

/**
 *
 * @author gabri
 */
public class Aula04 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.print("Digite um número de 2 dígitos: ");
        int num = scanner.nextInt();
        
       if (num < 10 || num > 99) {
        System.out.println("Número inválido!");
        } else {
            int dezena = num / 10; 
            int unidade = num % 10;
            System.out.println(dezena + " + " + unidade + " = " + (dezena + unidade));
    }
       
        scanner.close();
    }
}