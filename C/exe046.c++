#include <stdio.h>
#include <locale.h>
#include <ctype.h>
 
void converter(char *str) {
    // Itera pela string até o caractere nulo
    for (int num = 0; str[num] != '\0'; num++) {
        str[num] = toupper(str[num]);
    }
}
 
int main() {
    setlocale(LC_ALL, "Portuguese");
 
    char str[100];
    printf("Digite uma palavra: ");
    fgets(str, sizeof(str), stdin);
 
    converter(str);
 
    printf("A palavra em maiúsculas é: %s\n", str);
 
    return 0;
}