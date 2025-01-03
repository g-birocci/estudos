#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    char name[50]; // Aloca espaço para 50 caracteres (ajuste conforme necessário)
    char sobrenome[50];
    int data;

    printf("Digite o seu primeiro nome: ");
    fgets(name, sizeof(name), stdin);
    // Removendo a nova linha, caso tenha sido lida
    name[strcspn(name, "\n")] = '\0';

    printf("Digite o seu sobrenome: ");
    fgets(sobrenome, sizeof(sobrenome), stdin);
    sobrenome[strcspn(sobrenome, "\n")] = '\0';

    printf("Digite o seu ano de nascimento: ");
    scanf("%d", &data);

    printf("%s %s %d\n", name, sobrenome, data);

    return 0;
}