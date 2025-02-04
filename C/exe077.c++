#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    FILE *file; // Ponteiro para o arquivo
    char filename[] = "caracter-a-caracter.txt";

    // Criar ou sobrescrever o arquivo
    file = fopen(filename, "w");
    if (file == NULL) {
        printf("Erro ao criar o arquivo.\n");
        return 1;
    }

    // Escrever a frase caractere por caractere
    char texto[] = "Manipulação de ficheiros em C";
    for (int i = 0; texto[i] != '\0'; i++) {
        fputc(texto[i], file);
    }

    fclose(file);
    printf("Arquivo '%s' criado com sucesso.\n", filename);

    // Abrir o arquivo no modo de adição para acrescentar texto
    file = fopen(filename, "a");
    if (file == NULL) {
        printf("Erro ao abrir o arquivo para adição.\n");
        return 1;
    }

    // Acrescentar a linha completa ao arquivo
    fprintf(file, "\nÉ possível escrever uma linha completa de texto.\n");
    fclose(file);
    printf("Texto foi adicionado ao arquivo '%s'.\n", filename);

    // Reabrir o arquivo no modo de leitura para exibir o conteúdo completo
    file = fopen(filename, "r");
    if (file == NULL) {
        printf("Erro ao abrir o arquivo para leitura.\n");
        return 1;
    }

    // Ler e imprimir o conteúdo do arquivo
    char line[256];
    printf("\nConteúdo do arquivo:\n");
    while (fgets(line, sizeof(line), file)) {
        printf("%s", line);
    }

    fclose(file);
    
    return 0;
}