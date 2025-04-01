/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula01;
import java.util.Scanner;

/**
 *
 * @author gabri
 */
public class Aula01 {

    /**
     * @param args the command line arguments
     */
 public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Minha Calculadore");
        System.out.println("1 - Somar");
        System.out.println("2 - Subtrair");
        System.out.println("3 - Multiplicar");
        System.out.println("4 - Dividir");
        
        System.out.print("Digite o primeiro numero: ");
        double n1 = scanner.nextDouble();
        
        System.out.print("Digite o segundo numero: ");
        double n2 = scanner.nextDouble();
        
        System.out.print("Escolha a opção desejada: [1 a 4]");
        int op = scanner.nextInt();
        
        double resul = 0;
        
        switch(op) {
            case 1: 
                resul = n1 + n2;
                break;
                
            case 2:
                resul = n1 - n2;
                break;
                
            case 3:
                resul = n1 * n2;
                break;
                
            case 4: 
                if(n2 != 0) {
                    resul = n1 / n2;
                }
                else {
                    System.out.println("Erro: Não pode dividir por zero!");
                    return;
                }
                break;
                
            default:
                System.out.println("Opção inválida!");
                return;
        }
        
        System.out.println("O resultado é: " + resul);
        
        scanner.close();
        
    }
    
}