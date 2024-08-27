Algoritmo "media_aproveitamento"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/08/2024
Var
   // Seção de Declarações das variáveis
   n1, n2, media : real

Inicio
   // Seção de Comandos, procedimento, funções, operadores, etc...
   Escreva ("Digite a primeira nota: ")
   leia (n1)
   Escreva ("digite a segunda nota: ")
   leia (n2)
   media <- (n1+n2)/2
   se (media < 5) entao
      escreval("Reprovado media ", media:5:2)
      escreva("Seu aproveiveitamento foi F")
   senao
      se (media >= 5) e (media < 6) entao
         escreval("Reprovado, media ", media:5:2)
         escreva("Seu aproveiveitamento foi E")
      senao
         se (media >= 6) e (media < 7) entao
            escreval ("Aprovado, media ", media:5:2)
            escreva("Seu aproveiveitamento foi D")
         senao
            se (media >= 7) e (media < 8) entao
               escreval ("Aprovado, media", media:5:2)
               escreva("Seu aproveiveitamento foi C")
            senao
               se (media >= 8) e (media < 9) entao
                  escreval ("Aprovado, media", media:5:2)
                  escreva("Seu aproveiveitamento foi B")
               senao
                    escreval ("Aprovado, media", media:5:2)
               escreva("Seu aproveiveitamento foi A")
               fimse
            fimse
         fimse
      fimse
   fimse

Fimalgoritmo