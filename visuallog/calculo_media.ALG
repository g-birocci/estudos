Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
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
      Escreva ("Você está aprovado!!!")
   senao
        se (media <7) e (media > 5) entao
           Escreva ("você está de recuperação!!!")
        senao
           Escreva ("você está reprovado")
        fimse
   fimse


Fimalgoritmo