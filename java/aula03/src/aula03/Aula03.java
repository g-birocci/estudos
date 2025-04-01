/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula03;
import java.util.Scanner;
/**
 *
 * @author gabri
 */
public class Aula03 {

    /**
     * @param args the command line arguments
     */  
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("-- Tabuada -- ");
        System.out.print("Digite o numero da tabuada que vc deseja: ");
        int n = scanner.nextInt();
       
        for(int i = 0; i <= 10; i++) {
            System.out.println(n + " * " + i + " = " + (n * i));
        } 
        scanner.close();
    }
}
