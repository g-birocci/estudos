#include <stdio.h>
#include <locale.h>

struct DATA {
    int dia, mes, ano;
};

struct ALUNO {
    int codigo;
    char nome[100];
    struct DATA data_nasc;
};

void entrada_dados(ALUNO *aluno) {
    printf("Digite o código do aluno: ");
    scanf("%d", &aluno->codigo);

    printf("Digite o nome do aluno: ");
    scanf(" %[^\n]", aluno->nome);

    printf("Digite a data de nascimento (dd mm aaaa): ");
    scanf("%d %d %d", &aluno->data_nasc.dia, &aluno->data_nasc.mes, &aluno->data_nasc.ano);
}

void exibir_dados(const ALUNO *aluno) {
    printf("\nDados do Aluno:\n");
    printf("Código: %d\n", aluno->codigo);
    printf("Nome: %s\n", aluno->nome);
    printf("Data de Nascimento: %02d/%02d/%04d\n",
           aluno->data_nasc.dia, aluno->data_nasc.mes, aluno->data_nasc.ano);
}

int main() {
    setlocale(LC_ALL, "Portuguese");

    ALUNO aluno;

    entrada_dados(&aluno);
    exibir_dados(&aluno);

    return 0;
}
