#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <locale.h>

// Estrutura para armazenar os contatos em uma lista encadeada
typedef struct Contatos {
    char nome[30];       // Nome do contato (máximo de 29 caracteres + '\0')
    char numero[10];     // Número do contato (9 dígitos + '\0')
    char morada[40];     // Endereço do contato
    char email[50];      // Email do contato
    struct Contatos* next; // Ponteiro para o próximo contato na lista encadeada
} Contatos;

// Protótipos das funções
Contatos* novo_Contato(const char* nome, const char* numero, const char* morada, const char* email);
void carregar_contatos(const char* lista_decontatos, Contatos** contato);
void inserir_finallista(Contatos** contato, Contatos* novo);
void salvarcontatos(const char* lista_decontatos, Contatos* contato);
void procurar_contato(Contatos* lista);
void editar_contato(Contatos* lista, const char* valor);
void deletar_contato(Contatos** lista, const char* valor);
void imprimir_contatos(Contatos* contato);
void limparBuffer();

// Função para busca de string ignorando maiúsculas/minúsculas
char* strcasestr_custom(const char* haystack, const char* needle) {
    if (!*needle) return (char*)haystack; // Caso a string de busca seja vazia, retorna o início da base

    // Percorre cada caractere da base (haystack)
    for (; *haystack; haystack++) {
        if (tolower((unsigned char)*haystack) == tolower((unsigned char)*needle)) { // Comparação ignorando maiúsculas/minúsculas
            const char* h = haystack + 1;
            const char* n = needle + 1;
            while (*h && *n && tolower((unsigned char)*h) == tolower((unsigned char)*n)) {
                h++;
                n++;
            }
            if (!*n) return (char*)haystack; // Retorna o endereço da ocorrência
        }
    }
    return NULL; // Retorna NULL caso não encontre
}

// Função para criar um novo contato
Contatos* novo_Contato(const char* nome, const char* numero, const char* morada, const char* email) {
    Contatos* novo = (Contatos*)malloc(sizeof(Contatos)); // Aloca memória para o novo contato
    if (!novo) { // Verifica se a alocação foi bem-sucedida
        perror("Erro na alocação de memória");
        exit(1);
    }
    // Copia os valores para os campos da estrutura
    strcpy(novo->nome, nome);
    strcpy(novo->numero, numero);
    strcpy(novo->morada, morada);
    strcpy(novo->email, email);
    novo->next = NULL; // Inicializa o próximo como NULL
    return novo;
}

// Função para carregar contatos de um arquivo
void carregar_contatos(const char* lista_decontatos, Contatos** contato) {
    FILE* file = fopen(lista_decontatos, "r"); // Abre o arquivo em modo leitura
    if (!file) { // Caso o arquivo não exista
        printf("Arquivo não encontrado. Iniciando lista vazia.\n");
        return;
    }

    char linha[200]; // Buffer para armazenar cada linha do arquivo
    while (fgets(linha, sizeof(linha), file)) { // Lê cada linha do arquivo
        linha[strcspn(linha, "\n")] = '\0'; // Remove o caractere de nova linha

        char nome[30], numero[10], morada[40], email[50];
        // Faz o parsing da linha separando os campos
        if (sscanf(linha, "%29[^,],%9[^,],%39[^,],%49[^\n]", nome, numero, morada, email) == 4) {
            inserir_finallista(contato, novo_Contato(nome, numero, morada, email)); // Adiciona à lista
        }
    }

    fclose(file); // Fecha o arquivo
    printf("Contatos carregados!\n");
}

// Função para inserir um contato no final da lista
void inserir_finallista(Contatos** contato, Contatos* novo) {
    if (*contato == NULL) { // Caso a lista esteja vazia
        *contato = novo; // O novo contato será o primeiro
        return;
    }

    Contatos* atual = *contato;
    while (atual->next != NULL) { // Percorre até o final da lista
        atual = atual->next;
    }
    atual->next = novo; // Adiciona o novo contato no final
}

// Função para salvar os contatos no arquivo
void salvarcontatos(const char* lista_decontatos, Contatos* contato) {
    FILE* file = fopen(lista_decontatos, "w"); // Abre o arquivo em modo escrita
    if (!file) { // Verifica se a abertura foi bem-sucedida
        perror("Erro ao abrir arquivo");
        exit(EXIT_FAILURE);
    }

    Contatos* atual = contato;
    while (atual != NULL) { // Escreve cada contato no arquivo
        fprintf(file, "%s,%s,%s,%s\n", atual->nome, atual->numero, atual->morada, atual->email);
        atual = atual->next;
    }

    fclose(file); // Fecha o arquivo
}

// Função para buscar contatos na lista
void procurar_contato(Contatos* lista) {
    char valor[30];
    printf("Digite o nome ou email para buscar: ");
    fgets(valor, sizeof(valor), stdin);
    valor[strcspn(valor, "\n")] = '\0'; // Remove o caractere de nova linha

    Contatos* atual = lista;
    int encontrado = 0;
    while (atual != NULL) {
        // Busca por nome ou email (ignorando maiúsculas/minúsculas)
        if (strcasestr_custom(atual->nome, valor) || strcasestr_custom(atual->email, valor)) {
            printf("Nome: %s\nNumero: %s\nMorada: %s\nEmail: %s\n\n", atual->nome, atual->numero, atual->morada, atual->email);
            encontrado = 1;
        }
        atual = atual->next;
    }

    if (!encontrado) {
        printf("Nenhum contato encontrado com "%s".\n", valor);
    }
}

// Função para editar um contato na lista
void editar_contato(Contatos* lista, const char* valor) {
    Contatos* atual = lista;
    while (atual != NULL) {
        if (strcasestr_custom(atual->nome, valor)) { // Verifica se o nome corresponde
            printf("Editando contato: %s\n", atual->nome);

            printf("Novo nome: ");
            fgets(atual->nome, sizeof(atual->nome), stdin);
            atual->nome[strcspn(atual->nome, "\n")] = '\0';

            printf("Novo numero: ");
            fgets(atual->numero, sizeof(atual->numero), stdin);
            atual->numero[strcspn(atual->numero, "\n")] = '\0';

            printf("Nova morada: ");
            fgets(atual->morada, sizeof(atual->morada), stdin);
            atual->morada[strcspn(atual->morada, "\n")] = '\0';

            printf("Novo email: ");
            fgets(atual->email, sizeof(atual->email), stdin);
            atual->email[strcspn(atual->email, "\n")] = '\0';

            printf("Contato atualizado!\n");
            return;
        }
        atual = atual->next;
    }
    printf("Contato com nome "%s" nao encontrado.\n", valor);
}

// Função para deletar um contato da lista
void deletar_contato(Contatos** lista, const char* valor) {
    Contatos* atual = *lista;
    Contatos* anterior = NULL;

    while (atual != NULL) {
        if (strcasestr_custom(atual->nome, valor)) { // Verifica se o nome corresponde
            if (anterior == NULL) { // Caso seja o primeiro elemento da lista
                *lista = atual->next;
            } else {
                anterior->next = atual->next;
            }
            free(atual); // Libera a memória do contato deletado
            printf("Contato deletado com sucesso!\n");
            return;
        }
        anterior = atual;
        atual = atual->next;
    }
    printf("Contato com nome "%s" nao encontrado.\n", valor);
}

// Função para imprimir todos os contatos da lista
void imprimir_contatos(Contatos* contato) {
    if (!contato) {
        printf("Nenhum contato na lista.\n");
        return;
    }

    Contatos* atual = contato;
    while (atual != NULL) {
        printf("Nome: %s\nNumero: %s\nMorada: %s\nEmail: %s\n\n", atual->nome, atual->numero, atual->morada, atual->email);
        atual = atual->next;
    }
}

// Função para limpar o buffer de entrada
void limparBuffer() {
    int c;
    while ((c = getchar()) != '\n' && c != EOF);
}

// Função principal
int main() {
    setlocale(LC_ALL, "Portuguese"); // Configura o locale para suporte a caracteres acentuados

    Contatos* lista = NULL; // Inicializa a lista de contatos como vazia
    const char* arquivo = "contatos.txt"; // Nome do arquivo de contatos

    carregar_contatos(arquivo, &lista); // Carrega os contatos do arquivo

    int opcao;
    do {
        printf("\nMenu:\n");
        printf("1. Adicionar contato\n");
        printf("2. Listar contatos\n");
        printf("3. Buscar contato\n");
        printf("4. Editar contato\n");
        printf("5. Deletar contato\n");
        printf("6. Salvar e sair\n");
        printf("Escolha uma opcao: ");
        scanf("%d", &opcao);
        limparBuffer();

        switch (opcao) {
            case 1: {
                char nome[30], numero[10], morada[40], email[50];

                printf("Nome: ");
                fgets(nome, sizeof(nome), stdin);
                nome[strcspn(nome, "\n")] = '\0';

                printf("Numero: ");
                fgets(numero, sizeof(numero), stdin);
                numero[strcspn(numero, "\n")] = '\0';

                printf("Morada: ");
                fgets(morada, sizeof(morada), stdin);
                morada[strcspn(morada, "\n")] = '\0';

                printf("Email: ");
                fgets(email, sizeof(email), stdin);
                email[strcspn(email, "\n")] = '\0';

                inserir_finallista(&lista, novo_Contato(nome, numero, morada, email));
                break;
            }
            case 2:
                imprimir_contatos(lista);
                break;
            case 3:
                procurar_contato(lista);
                break;
            case 4: {
                char nome[30];
                printf("Digite o nome do contato a ser editado: ");
                fgets(nome, sizeof(nome), stdin);
                nome[strcspn(nome, "\n")] = '\0';
                editar_contato(lista, nome);
                break;
            }
            case 5: {
                char nome[30];
                printf("Digite o nome do contato a ser deletado: ");
                fgets(nome, sizeof(nome), stdin);
                nome[strcspn(nome, "\n")] = '\0';
                deletar_contato(&lista, nome);
                break;
            }
            case 6:
                salvarcontatos(arquivo, lista);
                printf("Contatos salvos. Saindo...\n");
                break;
            default:
                printf("Opcao invalida!\n");
        }
    } while (opcao != 6);

    return 0;
}
