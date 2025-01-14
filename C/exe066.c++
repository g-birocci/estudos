#include <stdio.h>

void bubbleSort(int *vetor, int tamanho) {
    int temp;
    for (int i = 0; i < tamanho - 1; i++) {
        for (int j = 0; j < tamanho - i - 1; j++) { 
            if (vetor[j] > vetor[j + 1]) { // Comparação
                
                temp = vetor[j];
                vetor[j] = vetor[j + 1];
                vetor[j + 1] = temp;
            }
        }
    }
}

void imprimirVetor(int *vetor, int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");
}

int main() {
    int vetor[] = {64, 34, 25, 12, 22, 11, 90};
    int tamanho = sizeof(vetor) / sizeof(vetor[0]);

    printf("Vetor antes da ordenação: \n");
    imprimirVetor(vetor, tamanho);

    bubbleSort(vetor, tamanho);

    printf("Vetor após a ordenação: \n");
    imprimirVetor(vetor, tamanho);

    return 0;
}
