Algoritmo "Detran"

Var
   nasc, ano, idade : inteiro
Inicio
   escreva ("Digite em que ano n�s estamos: ")
   leia (ano)
   escreva ("Digite em que ano voc� naceu: ")
   leia (nasc)
   idade <- ano - nasc
   se (idade >= 18) entao
      escreva("Est� apto a tirar a carta de condu��o")
   senao
      escreva("N�o tem idade para dirigir")
   fimse
   
Fimalgoritmo