Algoritmo "fatorial"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 28/08/2024
Var
   c, n, f : inteiro
   resp : caractere

Inicio

repita
   escreva ("Digite um numero: ")
   leia (n)
   c <- n
   f <- 1
   repita
      f <- f * c
      c <- c - 1
   ate (c < 1)
   escreval ("O valor fatorial de ", n, " � igual �", f)
   escreva ("Deseja continuar [s\n]")
   leia (resp)
   limpatela
ate resp = ("n")

Fimalgoritmo