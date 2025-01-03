#include <stdio.h>
#include <ctype.h>

#define MAX_SENHA 20

int main() {
    char senha[MAX_SENHA];
    int tem_maiuscula = 0, tem_minuscula = 0, tem_numero = 0, tem_especial = 0;

    printf("Digite a senha: ");
    fgets(senha, MAX_SENHA, stdin);
    senha[strcspn(senha, "\n")] = '\0';

    for (int i = 0; senha[i] != '\0'; i++) {
        if (isupper(senha[i])) {
            tem_maiuscula = 1;
        } else if (islower(senha[i])) {
            tem_minuscula = 1;
        } else if (isdigit(senha[i])) {
            tem_numero = 1;
        } else {
            tem_especial = 1;
        }
    }

    if (tem_maiuscula && tem_minuscula && tem_numero && tem_especial) {
        printf("A senha é segura.\n");
    } else {
        printf("A senha precisa de mais segurança.\n");
    }

    return 0;
}