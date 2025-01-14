#include <stdio.h>

int tamanho_char(char *str) {
    int cont = -1; // negativo
    while (*str != '\0') {
        cont++;
        str++;
    }
    return cont;
}

int main() {
    char string[100];

    printf("Digite uma string: ");
    fgets(string, sizeof(string), stdin);

    int tamanho = tamanho_char(string);
    printf("Essa string tem %d caracter\n", tamanho);

    return 0;
}