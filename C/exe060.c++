#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int vetor[] = {10, 11, 23, 70, 20, 9, 25, 34, 52, 1};
    int *ptr = vetor;
    int maior = 0;

    for (int i = 0; i < 9; i++) {
        if (*ptr > maior) {
            maior = *ptr;
        }
        ptr++;
    }
    printf("Maior valor: %d\n", maior);
    printf("Endereço de maior: %p\n", &maior);


    return 0;
}