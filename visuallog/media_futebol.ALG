Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/08/2024
Var
   // Se��o de Declara��es das vari�veis
   g1, g2, dif : inteiro

Inicio
   // Se��o de Comandos, procedimento, fun��es, operadores, etc...
   escreva ("Quantos gols o corinthinas? ")
   leia (g1)
   escreva ("Quantos gol dos porcos? ")
   leia (g2)
   dif <- g1 - g2
   se (dif = 0) entao
      escreval("Diren�a � ", dif)
      escreva("Status: empate")
   senao
      se (dif <=3) entao
         escreval("Diferen�a � ", dif)
         escreva("Status: Jogo Normal")
      senao
         escreval("Diferen�a � ", dif)
         escreva("Status: Goleada do caralho")
      fimse
   fimse

Fimalgoritmo