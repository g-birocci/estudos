#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <locale.h>

typedef struct Contatos {
    char nome[30];
    char numero[9]; // Usando char para facilitar manipulação
    char morada[40];
    char email[50];
    struct Contatos* next;
} Contatos;

// Função para criar um novo contato
Contatos* novo_Contato(const char* nome, const char* numero, const char* morada, const char* email) {
    Contatos* novo = (Contatos*)malloc(sizeof(Contatos));
    if (novo == NULL) {
        perror("Erro na alocação de memória");
        exit(1);
    }
    strcpy(novo->nome, nome);
    strcpy(novo->numero, numero);
    strcpy(novo->morada, morada);
    strcpy(novo->email, email);
    novo->next = NULL;
    return novo;
}

// Função para inserir um novo contato no final da lista
void inserir_finallista(Contatos** contato, Contatos* novo) {
    if (*contato == NULL) {
        *contato = novo;
        return;
    }
    Contatos* atual = *contato;
    while (atual->next != NULL) {
        atual = atual->next;
    }
    atual->next = novo;
}

// Função para imprimir todos os contatos
void imprimir_contatos(Contatos* contato) {
    if (contato == NULL) {
        printf("\nA lista de contatos está vazia.\n");
        return;
    }

    printf("\nLista de Contatos:\n");
    Contatos* atual = contato;
    while (atual != NULL) {
        printf("Nome: %s\n", atual->nome);
        printf("Número: %s\n", atual->numero);
        printf("Morada: %s\n", atual->morada);
        printf("Email: %s\n", atual->email);
        printf("--------------------------\n");
        atual = atual->next;
    }
}

// Função para limpar o buffer do teclado
void limparBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

// Função principal
int main() {
    setlocale(LC_ALL, "Portuguese");

    Contatos* lista = NULL; // Inicializa a lista de contatos como NULL
    int opcao;

    do {
        printf("\nGerenciador de Contatos\n");
        printf("1 -- Adicionar contato\n");
        printf("2 -- Listar contatos\n");
        printf("3 -- Atualizar contato\n");
        printf("4 -- Deletar contato\n");
        printf("0 -- Sair\n");
        printf("Digite a opção desejada: ");
        scanf("%d", &opcao);
        limparBuffer();

        switch (opcao) {
            case 1: { // Adicionar contato
                char nome[30], numero[9], morada[40], email[50];
                printf("Digite o nome do contato: ");
                fgets(nome, sizeof(nome), stdin);
                nome[strcspn(nome, "\n")] = '\0'; // Remove o caractere de nova linha

                printf("Digite o número do contato: ");
                fgets(numero, sizeof(numero), stdin);
                numero[strcspn(numero, "\n")] = '\0';

                printf("Digite a morada do contato: ");
                fgets(morada, sizeof(morada), stdin);
                morada[strcspn(morada, "\n")] = '\0';

                printf("Digite o email do contato: ");
                fgets(email, sizeof(email), stdin);
                email[strcspn(email, "\n")] = '\0';

                Contatos* novo = novo_Contato(nome, numero, morada, email);
                inserir_finallista(&lista, novo);
                printf("Contato adicionado com sucesso!\n");
                break;
            }

            case 2: // Listar contatos
                imprimir_contatos(lista);
                break;

            case 3: // Atualizar contato (ainda não implementado)
                printf("Opção 'Atualizar contato' ainda não implementada.\n");
                break;

            case 4: // Deletar contato (ainda não implementado)
                printf("Opção 'Deletar contato' ainda não implementada.\n");
                break;

            case 0: // Sair
                printf("Saindo do programa...\n");
                break;

            default:
                printf("Opção inválida. Tente novamente.\n");
        }

    } while (opcao != 0);

    // Libera a memória alocada
    Contatos* atual = lista;
    while (atual != NULL) {
        Contatos* proximo = atual->next;
        free(atual);
        atual = proximo;
    }

    return 0;
}