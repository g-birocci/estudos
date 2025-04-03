/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula15;
import java.util.Scanner;

class Cliente {
    private int numero;
    private String nome;
    private String endereco;
    private String telefone;

    public Cliente(int numero, String nome, String endereco, String telefone) {
        this.numero = numero;
        this.nome = nome;
        this.endereco = endereco;
        this.telefone = telefone;
    }

    public String getNome() {
        return nome;
    }
}

class Conta {
    private int numeroConta;
    private Cliente cliente;
    private double saldo;

    public Conta(int numeroConta, Cliente cliente, double saldoInicial) {
        this.numeroConta = numeroConta;
        this.cliente = cliente;
        this.saldo = saldoInicial;
    }

    // Consultar saldo
    public void consultarExtrato() {
        System.out.println("Saldo atual: R$ " + String.format("%.2f", saldo));
    }

    // Levantar dinheiro
    public void levantar(double valor) {
        if (valor > 0 && valor <= saldo) {
            saldo -= valor;
            System.out.println("Levantamento de £ "+ String.format("%.2f", valor) + " realizado com sucesso.");
            consultarExtrato();
        } else {
            System.out.println("Saldo insuficiente ou valor inválido.");
        }
    }

    // Depositar dinheiro
    public void depositar(double valor) {
        if (valor > 0) {
            saldo += valor;
            System.out.println("Depósito de R$ " + String.format("%.2f", valor) + " realizado com sucesso.");
            consultarExtrato();
        } else {
            System.out.println("Valor de depósito inválido.");
        }
    }
}
/**
 *
 * @author gabri
 */
public class Aula15 {

    private static Scanner scanner = new Scanner(System.in);
    private static Conta contaAtual = null; // Variável global para armazenar a conta atual

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // TODO code application logic here
       // Autenticação por PIN
        final int PIN_CORRETO = 1234; // PIN pré-definido para teste
        int tentativas = 0;
        boolean autenticado = false;

        while (tentativas < 3) {
            System.out.print("Digite o seu PIN: ");
            int pin = scanner.nextInt();

            if (pin == PIN_CORRETO) {
                autenticado = true;
                break;
            } else {
                tentativas++;
                System.out.println("PIN incorreto. Tentativas restantes: " + (3 - tentativas));
            }
        }

        if (!autenticado) {
            System.out.println("Número máximo de tentativas excedido.");
            scanner.close();
            return;
        }

        // Menu principal
        while (true) {
            System.out.println("\n--- MENU PRINCIPAL ---");
            System.out.println("1. Criar cliente e conta");
            System.out.println("2. Consultar extrato");
            System.out.println("3. Levantar dinheiro");
            System.out.println("4. Depositar dinheiro");
            System.out.println("5. Sair");
            System.out.print("Escolha uma opção: ");
            int opcao = scanner.nextInt();

            switch (opcao) {
                case 1:
                    criarClienteEConta();
                    break;
                case 2:
                    if (contaAtual != null) {
                        contaAtual.consultarExtrato();
                    } else {
                        System.out.println("Nenhuma conta criada ainda.");
                    }
                    break;
                case 3:
                    if (contaAtual != null) {
                        System.out.print("Digite o valor a levantar: ");
                        double valorLevantar = scanner.nextDouble();
                        contaAtual.levantar(valorLevantar);
                    } else {
                        System.out.println("Nenhuma conta criada ainda.");
                    }
                    break;
                case 4:
                    if (contaAtual != null) {
                        System.out.print("Digite o valor a depositar: ");
                        double valorDepositar = scanner.nextDouble();
                        contaAtual.depositar(valorDepositar);
                    } else {
                        System.out.println("Nenhuma conta criada ainda.");
                    }
                    break;
                case 5:
                    System.out.println("Saindo do programa...");
                    scanner.close();
                    return;
                default:
                    System.out.println("Opção inválida. Tente novamente.");
            }
        }
    }

    // Método para criar cliente e conta
    private static void criarClienteEConta() {
        try {
            System.out.print("Digite o número do cliente: ");
            int numeroCliente = scanner.nextInt();
            scanner.nextLine(); // Limpar buffer

            System.out.print("Digite o nome do cliente: ");
            String nomeCliente = scanner.nextLine();

            System.out.print("Digite o endereço do cliente: ");
            String enderecoCliente = scanner.nextLine();

            System.out.print("Digite o telefone do cliente: ");
            String telefoneCliente = scanner.nextLine();

            System.out.print("Digite o número da conta: ");
            int numeroConta = scanner.nextInt();

            System.out.print("Digite o saldo inicial da conta: ");
            double saldoInicial = scanner.nextDouble();

            Cliente cliente = new Cliente(numeroCliente, nomeCliente, enderecoCliente, telefoneCliente);
            contaAtual = new Conta(numeroConta, cliente, saldoInicial);

            System.out.println("Cliente e conta criados com sucesso!");
        } catch (Exception e) {
            System.out.println("Erro ao criar cliente e conta. Certifique-se de inserir os dados corretamente.");
            scanner.nextLine(); // Limpar buffer em caso de erro
        }
    }
}