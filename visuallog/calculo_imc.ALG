Algoritmo "semnome"
// Disciplina   : [Linguagem e Lógica de Programação]
// Professor   : Antonio Carlos Nicolodi
// Descrição   : Aqui você descreve o que o programa faz! (função)
// Autor(a)    : Nome do(a) aluno(a)
// Data atual  : 22/08/2024
Var
   // Seção de Declarações das variáveis
   peso, m, imc : real

Inicio
   Escreva ("Digite o seu peso: (kg)")
   leia(peso)
   Escreva("Digite a sua altura: (m)")
   leia(m)
   imc <- peso / (m * m)
   escreval ("IMC ", imc:5:2)
   se (imc < 17) entao
      escreva("Está muito abaixo do seu peso ideal.")
   senao
      se (imc > 17) e (imc <=  18.5) entao
         Escreva ("Está abaixo do peso.")
      senao
         se (imc >= 18.5) e (imc < 25) entao
            escreva("Você está no seu peso ideal.")
         senao
            se (imc >= 25) e (imc <30) entao
               escreva("Acima do peso")
            senao
               se (imc >= 30) e (imc < 35) entao
                  escreva("está com obesidade")
               senao
                  se (imc >=35) e (imc < 40) entao
                     escreva("Está com obesidade severa")
                  senao
                     escreva("Está com obesidade morbida")
                  fimse
               fimse
            fimse
         fimse
      fimse
   fimse

Fimalgoritmo