Algoritmo "Detran"

Var
   nasc, ano, idade : inteiro
Inicio
   escreva ("Digite em que ano nós estamos: ")
   leia (ano)
   escreva ("Digite em que ano você naceu: ")
   leia (nasc)
   idade <- ano - nasc
   se (idade >= 18) entao
      escreva("Está apto a tirar a carta de condução")
   senao
      escreva("Não tem idade para dirigir")
   fimse
   
Fimalgoritmo