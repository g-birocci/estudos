Algoritmo "contador inteligente"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 27/08/2024
Var
   n1, n2, cont : inteiro

Inicio
   escreva ("In�cio: ")
   leia (n1)
   escreva ("Fim: ")
   leia (n2)

   se (n1 <= n2) entao
      cont <- n1
      enquanto (cont <= n2) faca
         escreva (cont)
         cont <- cont + 1
      fimenquanto
   senao
      cont <- n1
      enquanto (cont >= n2) faca
         escreva (cont)
         cont <- cont - 1
      fimenquanto
   fimse

Fimalgoritmo
