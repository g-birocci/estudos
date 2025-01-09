#include <stdio.h>
#include <locale.h>

int maximo(n1, n2) {

}

int main() {
    setlocale(LC_ALL, "Portuguese");

    int n1;
    int n2;
    int *ptr;

    printf("Digite um numero: ");
    scanf("%d", &n1);
    printf("Digite outro numero: ");
    scanf("%d", &n2);

    int maior = maximo(n1, n2);



    return 0;
}
