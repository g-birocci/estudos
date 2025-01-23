#include <stdio.h>
#include <locale.h>

enum sexo {masculino = -10, feminino = -20};

int main () {
    
    int opcao = masculino;

    switch (opcao)
    {
    case masculino:
        printf("%d", masculino);
        break;
    case feminino:
        printf("%d", feminino);
    default:
        break;
    }

    return 0;
}
