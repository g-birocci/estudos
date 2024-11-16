#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "Portuguese");

    float resto;
    int segundo;
    int minuto;
    int hora;

    printf ("--Conversor para horas--\n");
    printf("--Digite os segundos que deseja converte: ");
    scanf("%d", &segundo);

    hora = segundo / 3600;        
    resto = segundo % 3600;
    minuto = (int)resto / 60;
    segundo = (int)resto % 60;

    //printf("%f\n", resto);
    printf("Este valor convertido fica com %d horas e %d minuto e %d segundos.\n", hora, minuto, segundo);
    

    return 0;
}
