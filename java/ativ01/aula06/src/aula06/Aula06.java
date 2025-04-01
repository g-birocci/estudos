/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula06;

/**
 *
 * @author gabri
 */
public class Aula06 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int a = 1;
        int b = 2;
        
        System.out.println("A = " + a);
        System.out.println("B = " + b);
        
        int troca = a;
        a = b;
        b = troca;
        
        System.out.println("Após a troca de variavel");
        System.out.println("A = " + a);
        System.out.println("B = " + b);
                
    }
    
}
