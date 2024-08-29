Algoritmo "contando_negativo"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 28/08/2024
Var
   // Seção de Declarações das variáveis
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
   escreval ("Foram digitados ", tn, "números negativos" )

Fimalgoritmo