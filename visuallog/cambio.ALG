Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 30/08/2024
Var
   // Se��o de Declara��es das vari�veis
   n1, cambio, tot : real
   cont, vezes : inteiro

Inicio
   cont <- 1
   escreva("QUanta vezes vc quer converte? ")
   leia (vezes)
   enquanto (cont <= vezes) faca
            escreval ("Digite o valor que deseja converter: ")
            leia (n1)
            cambio <- n1/4.5
            tot <- tot + cambio
            escreval("O valor do cambio ficou $", cambio:5:2,".")
            cont <- cont + 1
   fimenquanto
   escreva("O valor total do dinheiro convertido � ", tot:5:2)
Fimalgoritmo