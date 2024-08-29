Algoritmo "tabuada"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
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