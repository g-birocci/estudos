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

// Protótipos das funções, com isso eu evito erros na logica do programa.
Contatos* novo_Contato(const char* nome, const char* numero, const char* morada, const char* email);
void carregar_contatos(const char* lista_decontatos, Contatos** contato);
void inserir_finallista(Contatos** contato, Contatos* novo);
void salvarcontatos(const char* lista_decontatos, Contatos* contato);
void procurar_contato(const char* lista_decontatos, const char* valor);
void imprimir_contatos(Contatos* contato);
void limparBuffer();

// Definição das funções em sequencia
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

void carregar_contatos(const char* lista_decontatos, Contatos** contato) {
    FILE* file = fopen(lista_decontatos, "r");
    if (!file) {
        printf("Arquivo de contatos não encontrado. Iniciando com lista vazia.\n");
        return;
    }

    char linha[200];
    while (fgets(linha, sizeof(linha), file)) {
        linha[strcspn(linha, "\n")] = '\0'; // Remover caracteres de nova linha

        char nome[30], numero[9], morada[40], email[50];
        if (sscanf(linha, "%29[^,],%8[^,],%39[^,],%49[^\n]", nome, numero, morada, email) == 4) {
            Contatos* novo_contato = novo_Contato(nome, numero, morada, email);
            inserir_finallista(contato, novo_contato);
        } else {
            printf("Linha inválida no arquivo: %s\n", linha);
        }
    }

    fclose(file);
    printf("Contatos carregados com sucesso.\n");
}

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

// Restante do código...

//vou salavar os dados em um arquivo de texto
void salvarcontatos(const char* lista_decontatos, Contatos* contato) {
    FILE *file = fopen(lista_decontatos, "a");
    if (!file) {
        perror("Não foi possivel abrir o arquivo");
        exit(EXIT_FAILURE);
    }

    fprintf(file, "%s,%s,%s,%s\n", contato->nome, contato->numero, contato->morada, contato->email);
    fclose(file);
}

//eu vou ler o arquivo txt e procurar um contato pelo nome ou numero
void procurar_contato(const char* lista_decontatos, const char* valor) {
    FILE* file = fopen(lista_decontatos, "r");
    if (!file) {
        perror("Não foi possivel abrir o arquivo");
        exit(EXIT_FAILURE);
    }

    char linha[200];
    int encontrado = 0;

    while (fgets(linha, sizeof(linha), file)) 
    {
        Contatos contato;
        sscanf(linha, "%[^,],%[^,],%[^,],%[^\n]", contato.nome, contato.numero, contato.morada, contato.email);

        if(strstr(contato.nome , valor) != NULL || strstr(contato.numero, valor) != NULL) {
            printf("\nContato encontrado:\n");
            printf("Nome: %s\n", contato.nome);
            printf("Número: %s\n", contato.numero);
            printf("Morada: %s\n", contato.morada);
            printf("Email: %s\n", contato.email);
            encontrado = 1;
            break;
        }
    }

    if (!encontrado) {
        printf("\nContato com a chave '%s' não encontrado.\n", valor);
    }

    fclose(file);
    
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

int main() {
    setlocale(LC_ALL, "Portuguese");

    Contatos* lista = NULL;
    const char* lista_decontatos = "contatos.txt"; // Nome do arquivo

    // Carregar contatos salvos do arquivo
    carregar_contatos(lista_decontatos, &lista);

    int opcao;

    do {
        printf("\nGerenciador de Contatos\n");
        printf("1 -- Adicionar contato\n");
        printf("2 -- Listar contatos\n");
        printf("3 -- Procurar contato\n");
        printf("4 -- Deletar contato\n");
        printf("5 -- Editar um contato\n");
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

                while (1) {
                    printf("Digite o número do contato (9 dígitos): ");
                    fgets(numero, sizeof(numero), stdin);
                    numero[strcspn(numero, "\n")] = '\0'; // Remove o caractere de nova linha
            
                    // Verificar se o número tem exatamente 9 caracteres e todos são dígitos
                    if (strlen(numero) == 9 && strspn(numero, "0123456789") == 9) {
                        break; // Entrada válida, sair do loop
                    } else {
                        printf("Erro: O número deve conter exatamente 9 dígitos. Tente novamente.\n");
                    }
                }

                printf("Digite a morada do contato: ");
                fgets(morada, sizeof(morada), stdin);
                morada[strcspn(morada, "\n")] = '\0';

                printf("Digite o email do contato: ");
                fgets(email, sizeof(email), stdin);
                email[strcspn(email, "\n")] = '\0';

                Contatos* novo = novo_Contato(nome, numero, morada, email);
                inserir_finallista(&lista, novo);
                salvarcontatos(lista_decontatos, novo);
                printf("Contato adicionado com sucesso!\n");
                break;
            }

            case 2: // Listar contatos
                imprimir_contatos(lista);
                break;

            case 3: //Procurar contato
                char chave[30];
                printf("Digite o nome ou número para procurar: ");
                fgets(chave, sizeof(chave), stdin);
                chave[strcspn(chave, "\n")] = '\0';
                procurar_contato(lista_decontatos, chave);
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