#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "Portuguese");

    int num;

    printf("Digite o numero para saber se é PAR ou ímpar: ");
    scanf("%d", &num);

    if (num%2 == 0){
        printf("O %d é um numero PAR", num);
        
    }
        else {
            printf("O %d é um numero Ímpar", num);
        }
        
    return 0;
}