#include <stdio.h>
#include <string.h>


int check_strings(char *str1, char *str2) {
    return strcmp(str1, str2);
}


int main() {
    char string1[30], string2[30];

    printf("Digite a primeira string: ");
    fgets(string1, sizeof(string1), stdin);

    printf("Digite a segunda string: ");
    fgets(string2, sizeof(string2), stdin);

    int resultado = check_strings(string1, string2);

    if (resultado == 0) {
        printf("As strings são iguais.\n");
    } else {
        printf("As strings são diferentes.");
    }


    return 0;
}