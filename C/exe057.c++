#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int vetor[] = {10,20,30,40,50,60,70,80,90,100};

    int *ptr = vetor;

    for (int i = 0; i < 10; i++) {
        printf("%d\n", *(ptr + i));
    }

    ptr = &vetor[9];

    for (int i = 0; i < 10 ; i++) {
        printf("%d\n", *(ptr - i));
    }
    return 0;
}