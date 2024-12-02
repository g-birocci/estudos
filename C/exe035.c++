#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int n1;
    int count = 0;
    

    printf("Digite o valor a ser dividido: ");
    scanf("%d", &n1);

    if (n1 <= 0) {
        printf("Só é aceito numeros natural.");
        return 1;
    }

    for ( int i = 1; i < n1; i++) {
        if (n1 % i == 0) {
            printf("%d\n", i);
            count++;
        }        
    }
    printf("O numero %d é dividido por %d\n", n1, count);
    return 0;
}