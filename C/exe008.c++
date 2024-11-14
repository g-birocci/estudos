#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <iostream>
using namespace std;

int main () {
    setlocale(LC_ALL,"Portuguese");

    int op;
    float temperatura;
    float celcius;
    float fahrenheit;

    

    printf ("Qual temperatura deseja converte Celcius[1] ou Fahrenheit[2].");
    scanf("%i", &op);

    printf("Digite o valor da temperatura: ");
    scanf ("%f", &temperatura);


    if (op == 1) {
        celcius = (temperatura * 1.8 + 32);
        printf ("A temperatura em celcius é %.2f\n", celcius);
    }

    if (op == 2) {
        fahrenheit = (5.0 / 9.0) * (temperatura - 32);
        printf ("A temperatura em fahrenheit é %.2f\n", fahrenheit);
    }

    return 0;
}