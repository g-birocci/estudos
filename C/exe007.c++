#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <iostream>
using namespace std;

int main () {
    setlocale(LC_ALL,"Portuguese");

    float alturax;
    float alturay;
    float area_total;

    printf ("Primeiro valor x: ");
    scanf ("%f", &alturax);

    printf ("Segundo valor y: ");
    scanf ("%f", &alturay);

    area_total = (alturax * alturay);

    printf("A área total é: %.2f\n", area_total);


    return 0;
}