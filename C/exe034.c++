#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int tam;
    float soma = 0;
    float media = 0;

    printf("Digite quantas notas quer insirir: ");
    scanf("%d", &tam);
    
    int*vetor = (int*)malloc(tam*sizeof(int));

    for (int i = 0; i < tam; i++) {
        printf("Digite as notas entre 0 a 20: ");
        scanf("%d", &vetor[i]);
        soma += vetor[i];
    }

    media = soma / tam;
    
    if (media >= 9.5) {
    printf("Aluno Aprovado!\n");
    } else {
    printf("Aluno Reprovado!\n");
    }

    free(vetor);

return 0;
}