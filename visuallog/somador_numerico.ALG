Algoritmo "somador_numerico"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 30/08/2024
Var
   // Seção de Declarações das variáveis
   cont, valor, soma, maior : inteiro

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   cont <- 1
   soma <- 0
   enquanto (cont <= 5) faca
      escreva("Digite o primeiro valor: ")
      leia (valor)
      se (valor > maior) entao
         maior <- valor
      fimse
      soma <- soma + valor
      cont <- cont + 1
   fimenquanto
   escreval("O valor da soma é ", soma, "e o maior valor digitado foi ", maior)

Fimalgoritmo