#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    char nomes[5][20]; 

    for (int i = 0; i < 5; i++) { 
        printf("Digite o nome: ");
        scanf("%s", nomes[i]); 
    }

    for (int i = 0; i < 5; i++) { 
        printf("%s\n", nomes[i]);
    }

    return 0;
}