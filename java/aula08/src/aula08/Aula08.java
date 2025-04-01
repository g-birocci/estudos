/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula08;
import java.util.Scanner;

/**
 *
 * @author gabri
 */
public class Aula08 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        
        System.out.println("Digite o número do mês: ");
        int mes = scanner.nextInt();
        
        System.out.println("Digite o ano: ");
        int ano = scanner.nextInt();
        
        switch (mes) {
            case 1: case 3: case 5: case 7: case 8: case 10: case 12:
                System.out.println("31 dias");
                break;
                
            case 4: case 6: case 9: case 11:
                System.out.println("30 dias");
                break;

            case 2:
                if ((ano % 400 == 0) || (ano % 4 == 0 && ano % 100 != 0)) {
                    System.out.println("29 dias (Ano bissexto)");
                } else {
                    System.out.println("28 dias");
                }
                break;

            default:
                System.out.println("Mês inválido");
                break;
        }
    }
}
