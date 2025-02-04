#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

struct Funcionario {
    int codigo;
    char nome[100];
    char funcao[100];
};

int main() {
    setlocale(LC_ALL, "Portuguese");

    char filename[] = "funcionario.bin";

    FILE *file;

    struct Funcionario funcionario = {
        1, "Gabriel", "Programador"
    };

    file = fopen(filename, "wb");
    if (file == NULL) {
        printf("Erro ao criar o arquivo.\n");
        return 1;
    }

    fwrite(&funcionario, sizeof(struct Funcionario), 1, file);
    fclose(file);
    printf("Dados do funcionário foram salvos no arquivo '%s'.\n", filename);

    
    file = fopen(filename, "rb"); // Abrir o arquivo binário para leitura
    if (file == NULL) {
        printf("Erro ao abrir o arquivo.\n");
        return 1;
    }

    struct Funcionario funcionarioLido;

    fread(&funcionarioLido, sizeof(struct Funcionario), 1, file);
    fclose(file);

    printf("\nDados do funcionário lido do arquivo:\n");
    printf("Código: %d\n", funcionarioLido.codigo);
    printf("Nome: %s\n", funcionarioLido.nome);
    printf("Função: %s\n", funcionarioLido.funcao);

    return 0;
}