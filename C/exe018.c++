#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "Portuguese");

    float nota1;
    float nota2;
    float nota3;
    float resultado;

    printf("Digite as 3 notas (separadas por virgula)");
    scanf("%f, %f, %f",&nota1,&nota2,&nota3);

    resultado = (nota1 + nota2 + nota3)/3;

    if (resultado >= 9.5){
        printf("Aprovado");
    }
        else {
            printf("Reprovado");
        }

    return 0;
}
