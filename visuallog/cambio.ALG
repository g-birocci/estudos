Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 30/08/2024
Var
   // Seção de Declarações das variáveis
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
   escreva("O valor total do dinheiro convertido é ", tot:5:2)
Fimalgoritmo