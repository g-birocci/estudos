#include <stdio.h>
#include <locale.h>

void multiplica(int vetor[], int tamanho) {
    for (int i = 0; i < tamanho; i++) {
        vetor[i] *= 2;
    }

    printf("Vetor dentro da função após a multiplicação:\n");
    for (int i = 0; i < tamanho; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");
}

int main() {
    int n;
    printf("Digite o número de elementos: ");
    scanf("%d", &n);

    int vetor[n]; 

    printf("Digite os elementos do vetor:\n");
    for (int i = 0; i < n; i++) {
        scanf("%d", &vetor[i]);
    }

    printf("Vetor antes da chamada da função:\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");

    multiplica(vetor, n);

    printf("Vetor após a chamada da função (em main):\n");
    for (int i = 0; i < n; i++) {
        printf("%d ", vetor[i]);
    }
    printf("\n");

    return 0;
}