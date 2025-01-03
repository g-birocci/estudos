#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int maiornumero(int arr[], int tamanho) {
    int maior = arr[0];

    for (int i = 1; i < tamanho; i++) {
        if (arr[i] > maior) {
            maior = arr[i];
        }
    }

    return maior;
}

int main() {
    int arr[] = {3, 7, 2, 9, 5};
    int tamanho = sizeof(arr) / sizeof(arr[0]);

    int maiorElemento = maiornumero(arr, tamanho);

    printf("O maior elemento do array é: %d\n", maiorElemento);

    return 0;
}