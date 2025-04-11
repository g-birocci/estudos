/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package aula17;

/**
 *
 * @author gabri
 */
public class Aula17 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        // Criando um funcionário interno
        FuncInterno funcInterno = new FuncInterno("Gabriel", "Birocci", 12345, "Gerente");
        System.out.println("Funcionário Interno:");
        System.out.println("Primeiro Nome: " + funcInterno.getPrimeiroNome());
        System.out.println("Último Nome e Cargo: " + funcInterno.getUltimoNome());
        System.out.println("ID do Empregado: " + funcInterno.getIdEmpregado());

        // Criando um funcionário externo
        FuncExterno funcExterno = new FuncExterno(67890, "Consultoria");
        System.out.println("\nFuncionário Externo:");
        funcExterno.exibirDados();
    }
}

// Classe Pessoa
class Pessoa {
    // Atributos privados
    private String primeiroNome;
    private String ultimoNome;

    // Construtor
    public Pessoa(String primeiroNome, String ultimoNome) {
        this.primeiroNome = primeiroNome;
        this.ultimoNome = ultimoNome;
    }

    // Método do primeiro nome
    public String getPrimeiroNome() {
        return primeiroNome;
    }

    // Método do ultimo name
    public String getUltimoNome() {
        return ultimoNome;
    }
}

// Subclasse FuncInterno que herda de Pessoa
class FuncInterno extends Pessoa {
    // Atributos específicos de um funcionário interno
    private int idEmpregado;
    private String cargo;

    // Construtor
    public FuncInterno(String primeiroNome, String ultimoNome, int idEmpregado, String cargo) {
        super(primeiroNome, ultimoNome); // Chama o construtor da classe pai
        this.idEmpregado = idEmpregado;
        this.cargo = cargo;
    }

    // Método para obter o ID do empregado
    public int getIdEmpregado() {
        return idEmpregado;
    }

    // Sobrescrita do método getUltimoNome para incluir o cargo
    @Override
    public String getUltimoNome() {
        return super.getUltimoNome() + " - Cargo: " + cargo;
    }
}

// Classe FuncExterno que descreve um funcionário externo
class FuncExterno {
    // Atributos específicos de um funcionário externo
    private int codigo;
    private String tipoServico;

    // Construtor
    public FuncExterno(int codigo, String tipoServico) {
        this.codigo = codigo;
        this.tipoServico = tipoServico;
    }

    // Método para obter o código
    public int getCodigo() {
        return codigo;
    }

    // Método para obter o tipo de serviço prestado
    public String getTipoServico() {
        return tipoServico;
    }

    // Método para exibir os dados do funcionário externo
    public void exibirDados() {
        System.out.println("Funcionário Externo - Código: " + codigo + ", Tipo de Serviço: " + tipoServico);
    }
}