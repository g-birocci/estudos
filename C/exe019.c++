#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    float nota1, nota2, nota3, resultado;

    printf("Digite as 3 notas (separadas por espaço): ");
    scanf("%f %f %f", &nota1, &nota2, &nota3);

    resultado = (nota1 + nota2 + nota3) / 3;

    if (resultado < 8) {
        printf("Reprovado\n");
        printf("Média: %.2f\n", resultado);
    } 
    else if (resultado >= 8 && resultado < 9.5) {
        printf("Está de recurso\n");
        printf("Média: %.2f\n", resultado);
    } 
    else {
        printf("Está Aprovado!!!\n");
        printf("Média: %.2f\n", resultado);
    }

    return 0;
}
