#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int num1;
    int num2;
    int num3;
 

    printf("Digite os 3 números para saber qual é o maior (separados por espaço): ");
    scanf("%d %d %d", &num1, &num2, &num3);

    if (num1 != num2 && num2 != num3){
         printf("Este triangulo é escaleno ");
    }
        else if (num2 == num1 && num2 == num3){
            printf("Este triangulo é equilatero");
        }
            else {
                 printf("Este triangulo é isoseles");
            }   

    return 0;
}