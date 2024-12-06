#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int vetor[] = {0};
    int vezes;
    int n;

    printf("Informe quantos numeros vair ser inseridos: ");
    scanf("%d", &vezes);

    for (int i = 0; i < vezes; i++) {
        printf("Digite os valores aqui: ");
        scanf("%i", &vetor[n]);
    }

    printf("%i", vetor);

    return 0;
}
