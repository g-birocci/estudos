Algoritmo "tabuada"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 28/08/2024
Var
   cont, n, resp : inteiro

Inicio

   cont <- 1
   escreva ("Qual tabuada desejada ? ")
   leia (n)
   repita
   resp <- n * cont
      escreval (n, " X ", cont, " = ", resp)
      cont <- cont + 1
   ate (cont > 10)
Fimalgoritmo