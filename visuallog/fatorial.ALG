Algoritmo "fatorial"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
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
   escreval ("O valor fatorial de ", n, " é igual á", f)
   escreva ("Deseja continuar [s\n]")
   leia (resp)
   limpatela
ate resp = ("n")

Fimalgoritmo