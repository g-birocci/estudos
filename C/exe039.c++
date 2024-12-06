#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    void dados_matrix(int matrix[5][5]) {
        for (x = 0; x < 5; x++){
            for (y = 0; y <= x; y++) {
                printf("Digite o valor da posição: ")
                scanf("%i", matrix[x][y]);
            }
            printf("\n")
        }

        
    }
    return 0;
}