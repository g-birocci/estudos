Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/08/2024
Var
   n1, n2, media : real


Inicio
   Escreva ("Digite a primeira nota: ")
   leia (n1)
   Escreva ("Digite a segunda nota: ")
   leia (n2)
   media <- (n1 + n2) / 2
   se (media >=7) entao
      Escreva ("Voc� est� aprovado!!!")
   senao
        se (media <7) e (media > 5) entao
           Escreva ("voc� est� de recupera��o!!!")
        senao
           Escreva ("voc� est� reprovado")
        fimse
   fimse


Fimalgoritmo