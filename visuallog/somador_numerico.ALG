Algoritmo "somador_numerico"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 30/08/2024
Var
   // Se��o de Declara��es das vari�veis
   cont, valor, soma, maior : inteiro

Inicio
   // Se��o de Comandos, procedimento, fun��es, operadores, etc...
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
   escreval("O valor da soma � ", soma, "e o maior valor digitado foi ", maior)

Fimalgoritmo