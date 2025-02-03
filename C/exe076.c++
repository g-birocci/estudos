#include <stdio.h>
#include <stdlib.h>
#include <locale>


int main() {
    setlocale(LC_ALL, "Portuguese");

    FILE *file; //Vai ser o ponteiro pra o arquivo
    char filename[] = "ficheiro_c.txt";

    file = fopen(filename, "w"); //esse bloco verefica se vai criar corretamente o arquivo, (Sempre usar)
    if (file == NULL) {
        printf("Erro ao criar o arquivo");
        return 1;
    }

    return 0;
}