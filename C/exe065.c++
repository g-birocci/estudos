#include <stdio.h>

void copiar_vetor(int vetor_original[], int vetor_copia[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        vetor_copia[i] = vetor_original[i];
    }
}

void imprimir_vetor(int vetor[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");
}

int main() {
    int tamanho, vetor_original[100], vetor_copia[100];

    printf("Digite o tamanho do vetor: ");
    scanf("%d", &tamanho);

    printf("Digite os elementos do vetor original:\n");
    for (int i = 0; i < tamanho; i++) {
        scanf("%d", &vetor_original[i]);
    }

    copiar_vetor(vetor_original, vetor_copia, tamanho);

    printf("Vetor original: ");
    imprimir_vetor(vetor_original, tamanho);

    printf("Vetor cópia: ");
    imprimir_vetor(vetor_copia, tamanho);

    return 0;
}