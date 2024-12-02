#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int nt;
    int resul = 0;

    printf("Digite o nome da tabuada que deseja: ");
    scanf("%d", &nt);

    if (nt <= 0) {
        printf("Numero não aceito.");
        printf("Saindo do programa...");
        return 1;
    }

    for (int i = 1; i <= 10;i++) {
        resul = nt * i;

        printf("%d x %d = %d\n", nt, i , resul);

    }


    return 0;
}