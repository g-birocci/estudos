Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 28/08/2024
Var
   // Se��o de Declara��es das vari�veis
   cont, n, contdiv : inteiro

Inicio
   escreva ("Digite um numero: ")
   leia (n)
   cont <- 1
   contdiv <- 0
   repita
      escreval (Cont)
      se (n % cont = 0) entao
         contdiv <- contdiv + 1
      fimse
      cont <- cont + 1
   ate (cont > n)
   se (contdiv = 2) entao
      escreva ("Este � numero primo")
   senao
      escreva("N�o � um numero primo")
   fimse


Fimalgoritmo