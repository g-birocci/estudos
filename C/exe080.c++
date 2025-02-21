#include <stdio.h>
#include <stdlib.h>

int main() {
    FILE *file;

    // Abrindo um ficheiro para escrita
    file = fopen("exemplo.txt", "w");
    if (!file) {
        perror("Erro ao abrir o ficheiro");
        exit(EXIT_FAILURE);
    }

    // Escrevendo no ficheiro
    fprintf(file, "Olá, Gabriel!\n");
    fprintf(file, "Aprendendo ficheiros em C.\n");

    fclose(file); // Fechando o ficheiro após escrever

    // Abrindo o ficheiro para leitura
    file = fopen("exemplo.txt", "r");
    if (!file) {
        perror("Erro ao abrir o ficheiro");
        exit(EXIT_FAILURE);
    }

    // Lendo o ficheiro linha por linha
    char linha[100];
    while (fgets(linha, sizeof(linha), file)) {
        printf("%s", linha);
    }

    fclose(file); // Fechando o ficheiro após ler

    return 0;
}
