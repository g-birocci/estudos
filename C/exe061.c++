#include <stdio.h>
#include <locale.h>

int maximo(int *ptr, int *ptr1) {
    if (*ptr > *ptr1) { 
        return *ptr;
    }
    else if (*ptr <  *ptr1) {
        return *ptr1;
    }
    else {
        printf("Os numeros são iguais.");
        return *ptr;
    }

}

int main() {
    setlocale(LC_ALL, "Portuguese");

    int n1;
    int n2;
    
    printf("Digite um numero: ");
    scanf("%d", &n1);
    printf("Digite outro numero: ");
    scanf("%d", &n2);

    int *ptr = &n1;
    int *ptr1 = &n2;

    int maior = maximo(ptr, ptr1);

    printf("O numero %d é o maior.\n", maior);

    return 0;
}
