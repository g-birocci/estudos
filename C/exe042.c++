#include <stdio.h>
#include <locale.h>
 
int ehPar(int numero) {
    return numero % 2 == 0;
}
 
int main() {
    setlocale(LC_ALL, "Portuguese");
    int numero;
 
    printf("Digite um número inteiro: ");
    scanf("%d", &numero);
 
    if (ehPar(numero)) {
        printf("O número %d é par.\n", numero);
    } else {
        printf("O número %d é ímpar.\n", numero);
    }
 
    return 0;
}