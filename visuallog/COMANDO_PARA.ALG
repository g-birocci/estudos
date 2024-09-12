Algoritmo "comando_para"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 12/09/2024
Var
   v, c, nimp, tot : inteiro


Inicio
   tot <- 0
   nimp <-0
   para c <- 1 ate 5 faca
      escreva ("digite uma valor: ")
      leia (v)
      se (v>=0) e (v<=10) entao
         tot <- tot + 1
       fimse
         se (v%2=1) entao
            nimp <- nimp + v
         fimse

   fimpara
   escreval ("Ao todo foram ", tot, "valores entre 0 e 10")
   escreval ("Neste intervalor a soma de impares foi ", nimp)

Fimalgoritmo