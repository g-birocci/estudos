#include <stdio.h>
#include <locale.h>
 
int main() {
    setlocale(LC_ALL, "Portuguese");
 
    int vetor[10] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
 
    printf("Números pares no vetor:\n");
 
    for (int numero = 0; numero < 10; numero++) {
        if (vetor[numero] % 2 == 0) {
            printf("%d ", vetor[numero]);
        }
    }
 
    printf("\n");
    return 0;
}