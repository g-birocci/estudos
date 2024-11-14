#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <math.h>

int main () {
    setlocale(LC_ALL,"Portuguese");

    int num;
    float rest;
    int teste;

    printf ("Digite o numero que deseja dividir: ");
    scanf ("%d", &num);
    
    rest = num % 100;
    printf("%f", rest);
    printf("\n%d", num);
    

    teste = num / 100;
    printf("\n%d", teste);


    return 0;
}