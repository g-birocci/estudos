Algoritmo "semnome"
// Disciplina   : [Linguagem e L�gica de Programa��o]
// Professor   : Antonio Carlos Nicolodi
// Descri��o   : Aqui voc� descreve o que o programa faz! (fun��o)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/08/2024
Var
   // Se��o de Declara��es das vari�veis
   peso, m, imc : real

Inicio
   Escreva ("Digite o seu peso: (kg)")
   leia(peso)
   Escreva("Digite a sua altura: (m)")
   leia(m)
   imc <- peso / (m * m)
   escreval ("IMC ", imc:5:2)
   se (imc < 17) entao
      escreva("Est� muito abaixo do seu peso ideal.")
   senao
      se (imc > 17) e (imc <=  18.5) entao
         Escreva ("Est� abaixo do peso.")
      senao
         se (imc >= 18.5) e (imc < 25) entao
            escreva("Voc� est� no seu peso ideal.")
         senao
            se (imc >= 25) e (imc <30) entao
               escreva("Acima do peso")
            senao
               se (imc >= 30) e (imc < 35) entao
                  escreva("est� com obesidade")
               senao
                  se (imc >=35) e (imc < 40) entao
                     escreva("Est� com obesidade severa")
                  senao
                     escreva("Est� com obesidade morbida")
                  fimse
               fimse
            fimse
         fimse
      fimse
   fimse

Fimalgoritmo