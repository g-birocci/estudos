#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
#include <locale.h>

// Estrutura para armazenar os contatos em uma lista encadeada
typedef struct Contatos {
    char nome[30];       // Nome do contato (máximo de 29 caracteres + '\0')
    char numero[11];     // Número do contato (9 dígitos + '\0')
    char morada[40];     // Endereço do contato (máximo de 39 caracteres + '\0')
    char email[50];      // Email do contato (máximo de 49 caracteres + '\0')
    struct Contatos* next; // Ponteiro para o próximo contato na lista encadeada
} Contatos;

// Protótipos das funções
Contatos* novo_Contato(const char* nome, const char* numero, const char* morada, const char* email);
void carregar_contatos(const char* arquivo, Contatos** contato);
void inserir_finallista(Contatos** contato, Contatos* novo);
void salvarcontatos(const char* arquivo, Contatos* contato);
void procurar_contato(Contatos* lista);
void editar_contato(Contatos* lista);
void deletar_contato(Contatos** lista, const char* valor);
void imprimir_contatos(Contatos* contato);
void limparBuffer();
char* strcasestr_custom(const char* haystack, const char* needle);

// Função para buscar uma substring ignorando maiúsculas/minúsculas
char* strcasestr_custom(const char* haystack, const char* needle) {
    if (!*needle) return (char*)haystack; // Se a string de busca for vazia, retorna o início da base

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

    novo->next = NULL; // Inicializa o ponteiro "next" como NULL
    return novo;
}

// Função para carregar contatos de um arquivo
void carregar_contatos(const char* arquivo, Contatos** contato) {
    FILE* file = fopen(arquivo, "r"); // Abre o arquivo em modo leitura
    if (!file) { // Caso o arquivo não exista
        printf("Arquivo não encontrado. Iniciando lista vazia.\n");
        return;
    }

    char linha[200]; // Buffer para armazenar cada linha do arquivo
    while (fgets(linha, sizeof(linha), file)) { // Lê cada linha do arquivo
        linha[strcspn(linha, "\n")] = '\0'; // Remove o caractere de nova linha

        char nome[30], numero[11], morada[40], email[50];
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
void salvarcontatos(const char* arquivo, Contatos* contato) {
    FILE* file = fopen(arquivo, "w"); // Abre o arquivo em modo escrita
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
    int opcao; // Armazena a escolha do usuário (1 - Nome, 2 - Número, 3 - Voltar)

    do {
        printf("\nSubmenu de Busca:\n");
        printf("1. Buscar por Nome\n");
        printf("2. Buscar por Número\n");
        printf("3. Voltar ao Menu Principal\n");
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);
        limparBuffer(); // Limpa o buffer de entrada

        if (opcao == 1 || opcao == 2) {
            char valor[30]; // Buffer para armazenar o termo de busca
            printf("Digite o termo para buscar: ");
            fgets(valor, sizeof(valor), stdin);
            valor[strcspn(valor, "\n")] = '\0'; // Remove o caractere de nova linha

            Contatos* atual = lista;
            int encontrado = 0;

            while (atual != NULL) {
                if (opcao == 1 && strcasestr_custom(atual->nome, valor)) { // Busca pelo nome
                    printf("Nome: %s\nNúmero: %s\nMorada: %s\nEmail: %s\n\n",
                           atual->nome, atual->numero, atual->morada, atual->email);
                    encontrado = 1;
                } else if (opcao == 2 && strcasestr_custom(atual->numero, valor)) { // Busca pelo número
                    printf("Nome: %s\nNúmero: %s\nMorada: %s\nEmail: %s\n\n",
                           atual->nome, atual->numero, atual->morada, atual->email);
                    encontrado = 1;
                }
                atual = atual->next;
            }

            if (!encontrado) {
                printf("Nenhum contato encontrado com \"%s\".\n", valor);
            }
        } else if (opcao != 3) {
            printf("Opção inválida. Tente novamente.\n");
        }

    } while (opcao != 3); // Continua no submenu até o usuário escolher voltar
}

// Função para editar um contato na lista
void editar_contato(Contatos* lista) {
    char nome[30];
    printf("Digite o nome do contato a ser editado: ");
    fgets(nome, sizeof(nome), stdin);
    nome[strcspn(nome, "\n")] = '\0'; // Remove o caractere de nova linha

    Contatos* atual = lista;
    int contador = 0; // Contador para numerar os contatos encontrados
    Contatos** matches = NULL; // Array para armazenar os contatos encontrados

    // Procura todos os contatos que correspondem ao nome fornecido
    while (atual != NULL) {
        if (strcasestr_custom(atual->nome, nome)) { // Verifica se o nome corresponde
            contador++;
            matches = realloc(matches, contador * sizeof(Contatos*)); // Redimensiona o array
            matches[contador - 1] = atual; // Adiciona o contato ao array
        }
        atual = atual->next;
    }

    if (contador == 0) {
        printf("Nenhum contato encontrado com o nome \"%s\".\n", nome);
        free(matches); // Libera o array caso nenhum contato seja encontrado
        return;
    }

    // Exibe os contatos encontrados com seus números
    printf("\nContatos encontrados:\n");
    for (int i = 0; i < contador; i++) {
        printf("%d. Nome: %s\n   Número: %s\n   Morada: %s\n   Email: %s\n",
               i + 1, matches[i]->nome, matches[i]->numero, matches[i]->morada, matches[i]->email);
    }

    // Solicita ao usuário que escolha um contato para editar
    int escolha;
    printf("Escolha o número do contato que deseja editar (ou 0 para cancelar): ");
    scanf("%d", &escolha);
    limparBuffer(); // Limpa o buffer de entrada

    if (escolha < 1 || escolha > contador) {
        if (escolha != 0) {
            printf("Opção inválida. Edição cancelada.\n");
        }
        free(matches); // Libera o array
        return;
    }

    // Obtém o contato selecionado
    Contatos* contato_selecionado = matches[escolha - 1];

    // Permite ao usuário editar os dados do contato
    printf("Editando contato: %s\n", contato_selecionado->nome);

    // Validar e ler o nome
    printf("Novo nome (%s): ", contato_selecionado->nome);
    fgets(contato_selecionado->nome, sizeof(contato_selecionado->nome), stdin);
    contato_selecionado->nome[strcspn(contato_selecionado->nome, "\n")] = '\0';

    // Validar e ler o número (deve ter exatamente 9 dígitos)
    do {
        printf("Novo número (%s): ", contato_selecionado->numero);
        fgets(contato_selecionado->numero, sizeof(contato_selecionado->numero), stdin);
        contato_selecionado->numero[strcspn(contato_selecionado->numero, "\n")] = '\0';

        if (strlen(contato_selecionado->numero) != 9 || !strspn(contato_selecionado->numero, "0123456789")) {
            printf("Erro: O número deve conter exatamente 9 dígitos numéricos.\n");
        }
    } while (strlen(contato_selecionado->numero) != 9 || !strspn(contato_selecionado->numero, "0123456789"));

    // Validar e ler a morada
    printf("Nova morada (%s): ", contato_selecionado->morada);
    fgets(contato_selecionado->morada, sizeof(contato_selecionado->morada), stdin);
    contato_selecionado->morada[strcspn(contato_selecionado->morada, "\n")] = '\0';

    // Validar e ler o email (deve conter "@")
    do {
        printf("Novo email (%s): ", contato_selecionado->email);
        fgets(contato_selecionado->email, sizeof(contato_selecionado->email), stdin);
        contato_selecionado->email[strcspn(contato_selecionado->email, "\n")] = '\0';

        if (strchr(contato_selecionado->email, '@') == NULL) {
            printf("Erro: O email deve conter o caractere '@'.\n");
        }
    } while (strchr(contato_selecionado->email, '@') == NULL);

    printf("Contato atualizado!\n");

    free(matches); // Libera o array
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
    printf("Contato com nome \"%s\" não encontrado.\n", valor);
}

// Função para imprimir todos os contatos da lista
void imprimir_contatos(Contatos* contato) {
    if (!contato) {
        printf("Nenhum contato na lista.\n");
        return;
    }

    Contatos* atual = contato;
    while (atual != NULL) {
        printf("Nome: %s\nNúmero: %s\nMorada: %s\nEmail: %s\n\n",
               atual->nome, atual->numero, atual->morada, atual->email);
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
        printf("Escolha uma opção: ");
        scanf("%d", &opcao);
        limparBuffer();

        switch (opcao) {
            case 1: { // Adicionar contato
                char nome[30], numero[11], morada[40], email[50];

                printf("Nome: ");
                fgets(nome, sizeof(nome), stdin);
                nome[strcspn(nome, "\n")] = '\0';

                // Validar e ler o número (deve ter exatamente 9 dígitos)
                do {
                    printf("Número: ");
                    fgets(numero, sizeof(numero), stdin);
                    numero[strcspn(numero, "\n")] = '\0';

                    if (strlen(numero) != 9 || !strspn(numero, "0123456789")) {
                        printf("Erro: O número deve conter exatamente 9 dígitos numéricos.\n");
                    }
                } while (strlen(numero) != 9 || !strspn(numero, "0123456789"));

                printf("Morada: ");
                fgets(morada, sizeof(morada), stdin);
                morada[strcspn(morada, "\n")] = '\0';

                // Validar e ler o email (deve conter "@")
                do {
                    printf("Email: ");
                    fgets(email, sizeof(email), stdin);
                    email[strcspn(email, "\n")] = '\0';

                    if (strchr(email, '@') == NULL) {
                        printf("Erro: O email deve conter o caractere '@'.\n");
                    }
                } while (strchr(email, '@') == NULL);

                inserir_finallista(&lista, novo_Contato(nome, numero, morada, email));
                break;
            }
            case 2: // Listar contatos
                imprimir_contatos(lista);
                break;
            case 3: // Buscar contato
                procurar_contato(lista);
                break;
            case 4: // Editar contato
                editar_contato(lista);
                break;
            case 5: { // Deletar contato
                char nome[30];
                printf("Digite o nome do contato a ser deletado: ");
                fgets(nome, sizeof(nome), stdin);
                nome[strcspn(nome, "\n")] = '\0';
                deletar_contato(&lista, nome);
                break;
            }
            case 6: // Salvar e sair
                salvarcontatos(arquivo, lista);
                printf("Contatos salvos. Saindo...\n");
                break;
            default:
                printf("Opção inválida!\n");
        }
    } while (opcao != 6);

    // Libera a memória alocada para a lista
    Contatos* atual = lista;
    while (atual != NULL) {
        Contatos* prox = atual->next;
        free(atual);
        atual = prox;
    }

    return 0;
}