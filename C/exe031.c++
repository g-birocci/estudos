#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int vetor[10] = {0};
    int soma = 0, notas_inseridas = 0;
    int maior = 0, menor = 0; 
    int tamanho = sizeof(vetor) / sizeof(vetor[0]);
    int opcao;

    while (1) {
        printf("\n1. Inserir notas\n");
        printf("2. Média das notas digitadas\n");
        printf("3. Imprimir vetor inverso\n");
        printf("4. Maior e menor nota\n");
        printf("5. Sair\n");
        printf("Escolha o que deseja fazer: ");
        scanf("%d", &opcao);

        switch (opcao) {
            case 1:
                printf("Digite as %d notas (entre 0 e 20):\n", tamanho);
                for (int i = 0; i < tamanho; i++) {
                    do {
                        printf("Nota %d: ", i + 1);
                        scanf("%d", &vetor[i]);
                        if (vetor[i] < 0 || vetor[i] > 20) {
                            printf("Nota inválida! Digite um valor entre 0 e 20.\n");
                        }
                    } while (vetor[i] < 0 || vetor[i] > 20);
                }
                notas_inseridas = 1; // Marca que as notas foram inseridas
                break;

            case 2:
                if (!notas_inseridas) {
                    printf("Erro: Nenhuma nota foi inserida ainda.\n");
                    break;
                }
                soma = 0;
                for (int i = 0; i < tamanho; i++) {
                    soma += vetor[i];
                }
                printf("A média das notas é: %.2f\n", (float)soma / tamanho);
                break;

            case 3:
                if (!notas_inseridas) {
                    printf("Erro: Nenhuma nota foi inserida ainda.\n");
                    break;
                }
                printf("Vetor invertido:\n");
                for (int i = tamanho - 1; i >= 0; i--) {
                    printf("%d ", vetor[i]);
                }
                printf("\n");
                break;

            case 4:
                if (!notas_inseridas) {
                    printf("Erro: Nenhuma nota foi inserida ainda.\n");
                    break;
                }
                maior = vetor[0];
                menor = vetor[0];
                for (int i = 1; i < tamanho; i++) {
                    if (vetor[i] > maior) maior = vetor[i];
                    if (vetor[i] < menor) menor = vetor[i];
                }
                printf("Maior nota: %d\n", maior);
                printf("Menor nota: %d\n", menor);
                break;

            case 5:
                printf("Saindo... Até logo!\n");
                return 0;

            default:
                printf("Opção inválida! Tente novamente.\n");
                break;
        }
    }

    return 0;
}
