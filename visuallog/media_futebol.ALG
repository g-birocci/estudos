Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/08/2024
Var
   // Seção de Declarações das variáveis
   g1, g2, dif : inteiro

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   escreva ("Quantos gols o corinthinas? ")
   leia (g1)
   escreva ("Quantos gol dos porcos? ")
   leia (g2)
   dif <- g1 - g2
   se (dif = 0) entao
      escreval("Dirença é ", dif)
      escreva("Status: empate")
   senao
      se (dif <=3) entao
         escreval("Diferença é ", dif)
         escreva("Status: Jogo Normal")
      senao
         escreval("Diferença é ", dif)
         escreva("Status: Goleada do caralho")
      fimse
   fimse

Fimalgoritmo