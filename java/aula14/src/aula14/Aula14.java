/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula14;



class Cliente { //Primeiro eu crio a classe do cliente
    private int num;
    private String nome;
    private String endereco;
    private String tel;
    
    //Faço o constrututor da classe cliente
    public Cliente(int num, String nome, String endereco, String tel) {
        this.num = num;
        this.nome = nome;
        this.endereco = endereco;
        this.tel = tel;
    }
    
    public String getnome() {
        return nome;
    }
    
    //Crio o metodo pra mostrar os daddos iguel o python
    
    public void mostrarinfo(String op) {
        if (op.equals("r")) {
            System.out.println("Numero: " + num + ", Nome: " + nome);
        } else if (op.equals("t")) {
            System.out.println("Numero: " + num);
            System.out.println("Nome: " + nome);
            System.out.println("Endereço: " + endereco);
            System.out.println("Telefone: " + tel);
        } else {
            System.out.println("Opção inválida!");
        }
    }
}

class Conta {
    private int numconta;
    private Cliente cliente; //Estou usando o objeto associando ele a conta
    private double saldo;
    
    //Contrutor 
    public Conta(int numconta, Cliente cliente, double saldo) {
        this.numconta = numconta;
        this.cliente = cliente;
        this.saldo = saldo;
    }
    
    public void mostrarinfoconta() {
        System.out.println("Numero da conta: " + numconta);
        System.out.println("Cliente: " + cliente.getnome());
        System.out.println("Saldo: £" + String.format("%.2f", saldo));
    } 
}
/**
 *
 * @author gabri
 */
public class Aula14 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
        Cliente cliente1 = new Cliente(1, "gabriel", "Rua de camoes", "999888000");
        
        Conta conta1 = new Conta(1001, cliente1, 10000.00);
        Conta conta2 = new Conta(1002, cliente1, 20000.00);
        
        System.out.println(" r - Dados resumidos");
        cliente1.mostrarinfo("r");
        
        System.out.println("\n t - Dados Completos");
        cliente1.mostrarinfo("t");
        
        System.out.println("Info da conta 1: ");
        conta1.mostrarinfoconta();
        
        System.out.println("Info da conta 2. ");
        conta1.mostrarinfoconta();
        
    }
    
}
