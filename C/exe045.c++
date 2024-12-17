#include <stdio.h>
#include <locale.h>
#include <ctype.h>
 
int contar(char *str) {
    int count = 0;
 
    for (int num = 0; str[num] != '\0'; num++) {
        if (isupper(str[num])) {
            count++;
        }
    }
 
    return count;
}
 
int main() {
    setlocale(LC_ALL, "Portuguese");
 
    char str[100];
    printf("Digite uma palavra: ");
    fgets(str, sizeof(str), stdin);
 
    int maiusculos = contar(str);
 
    printf("A quantidade de caracteres maiúsculos na palavra é: %d\n", maiusculos);

    return 0;
}