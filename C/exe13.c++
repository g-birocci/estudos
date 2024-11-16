#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "Portuguese");

    int num;
    int rest100, rest50, rest20, rest10;
    int notas100, notas50, notas20, notas10, notas5;

    printf("Digite o número que deseja dividir: ");
    scanf("%d", &num);

    notas100 = num / 100;
    rest100 = num % 100;
    printf("Número de notas de 100: %d\n", notas100);

    notas50 = rest100 / 50;
    rest50 = rest100 % 50;
    printf("Número de notas de 50: %d\n", notas50);

    notas20 = rest50 / 20;
    rest20 = rest50 % 20;
    printf("Número de notas de 20: %d\n", notas20);

    notas10 = rest20 / 10;
    rest10 = rest20 % 10;
    printf("Número de notas de 10: %d\n", notas10);

    notas5 = rest10 / 5;
    printf("Número de notas de 5: %d\n", notas5);

    return 0;
}
