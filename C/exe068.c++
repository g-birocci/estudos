#include <stdio.h>
#include <locale.h>
#include <string.h>

struct Cliente {
    char nome[70];
    char email[50];
};

void mostrar_cliente(struct Cliente clientes[], int vezes) {
    printf("\n=== Lista de Clientes ===\n");
    for (int i = 0; i < vezes; i++) {
        printf("\nCliente %d:\n", i + 1);
        printf("Nome: %s\n", clientes[i].nome);
        printf("E-mail: %s\n", clientes[i].email);
    }
}

void editar_cliente(struct Cliente clientes[], int vezes, char procurado[]) {
    for (int i = 0; i < vezes; i++) {
        if (strcmp(clientes[i].nome, procurado) == 0) {
            printf("\n--- Editando Cliente %s ---\n", clientes[i].nome);
            printf("Digite o novo nome: ");
            scanf(" %[^\n]", clientes[i].nome);
            printf("Digite o novo e-mail: ");
            scanf(" %[^\n]", clientes[i].email);
            printf("Cliente atualizado com sucesso!\n");
            return;
        }
    }
    printf("Cliente não encontrado!\n");
}

void excluir_cliente(struct Cliente clientes[], int *vezes, char procurado[]) {
    for (int i = 0; i < *vezes; i++) {
        if (strcmp(clientes[i].nome, procurado) == 0) {
            for (int j = i; j < *vezes - 1; j++) {
                clientes[j] = clientes[j + 1]; // Move os cliente para apagar
            }
            (*vezes)--; 
            printf("Cliente excluído!\n");
            return;
        }
    }
    printf("Cliente não encontrado!\n");
}

int main() {
    setlocale(LC_ALL, "Portuguese");

    int vezes, op;
    printf("Quantos clientes você quer adicionar: ");
    scanf("%d", &vezes);

    struct Cliente clientes[vezes];

    for (int i = 0; i < vezes; i++) {
        printf("\n*** Cliente %d ***\n", i + 1);
        printf("Digite o nome do cliente: ");
        scanf(" %[^\n]", clientes[i].nome); 
        printf("Digite o e-mail do cliente: ");
        scanf(" %[^\n]", clientes[i].email);
    }

    do {
        printf("\n=== Menu ===\n");
        printf("1 -- Exibir Clientes\n");
        printf("2 -- Editar Cliente\n");
        printf("3 -- Excluir Cliente\n");
        printf("4 -- Sair\n");
        printf("Escolha uma opção: ");
        scanf("%d", &op);

        switch (op) {
            case 1: 
                mostrar_cliente(clientes, vezes);
                break;

            case 2: { 
                char procurado[70];
                printf("Digite o nome do cliente que deseja editar: ");
                scanf(" %[^\n]", procurado);
                editar_cliente(clientes, vezes, procurado);
                break;
            }

            case 3: {
                char procurado[70];
                printf("Digite o nome do cliente que deseja excluir: ");
                scanf(" %[^\n]", procurado);
                excluir_cliente(clientes, &vezes, procurado);
                break;
            }

            case 4:
                printf("Saindo...\n");
                break;

            default:
                printf("Opção inválida!\n");
        }
    } while (op != 4);
    
    return 0;
}
