Algoritmo "contando_negativo"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 28/08/2024
Var
   // Se��o de Declara��es das vari�veis
   n, c, tn : inteiro

Inicio
      c <- 1
      tn <- 0
   repita
      Escreva ("Digite um numero: ")
      leia (n)
      se (n<0) entao
         tn <- tn + 1
      fimse
      c <- c + 1
   ate (c > 5)
   escreval ("Foram digitados ", tn, "n�meros negativos" )

Fimalgoritmo