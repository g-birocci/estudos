#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "Portuguese");

    int num1;
    int num2;
    int resul;
    int soma;

    printf("Digite um numero: ");
    scanf("%d", &num1);
    printf("Digite outro numero: ");
    scanf("%d", &num2);

    resul = num1 * num2;
    soma = num1 + num2;

    if (resul <= 1000){
        printf("A resultado é %d", resul);
    }
        else {
            printf("A soma é %d", soma);
        }
    return 0;
}
