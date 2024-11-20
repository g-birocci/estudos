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

    if (num1 >= num2 && num1 >= num3){
         printf("O maior numero é %d", num1);
    }
        else if (num2 >= num1 && num2 >= num3){
            printf("O maior numero é %d", num2);
        }
            else {
                 printf("O maior numero é %d", num3);
            }   

    return 0;
}