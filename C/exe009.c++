#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <iostream>
using namespace std;

int main () {
    setlocale(LC_ALL,"Portuguese");

    int idade;
    float altura;
    float peso;
    float imc;

    printf ("Vamos calcular o seu IMC");
    printf ("Digite a sua idade: ");
    scanf ("%i", &idade);

    printf ("Digite a sua altura: ");
    scanf ("%f", &altura);

    printf ("Digite o seu peso [kg]: ");
    scanf ("%f", &peso);

    imc = peso/(altura * altura); 
    printf("%.2f", imc);

    if (imc < 18.5) {
        printf ("Você esta abaixo do peso. ");
    }

        else if (imc < 25) {
         printf ("Você esta com peso ideal. ");
        }

            else if (imc < 30) {
            printf ("Você esta sobrepeso. ");
            }

                else if (imc < 35) {
                printf ("Você está com obesidade grau 1. ");
                }

                    else if (imc < 40) {
                    printf ("Você está com obesidade grau 2. ");
                    }

                        else {
                        printf ("Você está com obesidade grau 3 (mórbida). ");
                        }

    return 0;
}