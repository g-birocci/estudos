Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 27/08/2024
Var
   n, s, m, cont : inteiro


Inicio
   cont <- 1
   s <- 0
   enquanto (cont <= 5) faca
      escreva("Escreva uma valor, ")
      leia (n)
      se (n > m) entao
         m <- n
      fimse
      escreval (cont)
      cont <- cont + 1
      s <- s + n
   fimenquanto
   escreval ("A soma dos numeros �", s)
   escreva ("O maior numero �", m)

Fimalgoritmo