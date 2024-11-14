#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <math.h>

int main () {
    setlocale(LC_ALL,"Portuguese");

    int ax;
    int ay;
    int bx;
    int by;

    float distancia;

    printf ("Digite o valor do primeiro ponto: ");
    scanf ("%d, %d", &ax, &ay);

    printf ("Difite o valor do segundo ponto: ");
    scanf ("%d, %d", &bx, &by);

    distancia = sqrt(pow((bx - ax),2) + pow((by - ay),2));

    printf("%.2f", distancia);

    return 0;
}