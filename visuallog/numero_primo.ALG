Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 28/08/2024
Var
   // Seção de Declarações das variáveis
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
      escreva ("Este é numero primo")
   senao
      escreva("Não é um numero primo")
   fimse


Fimalgoritmo