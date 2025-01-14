#include <stdio.h>
#include <locale.h>
#include <string.h>

struct Produto {
    char id; 
    char nome[30]; 
    int preco;
    int quantidade;
};

int main() {
    setlocale(LC_ALL, "Portuguese");

    struct Produto produtos[4] = {
        {01, "Iphone 11", 2000, 4},
        {02, "Iphone 12", 2300, 2},
        {03, "Iphone 13", 2400, 5},
        {04, "Iphone 14", 2600, 3}
    };

    for (int i = 0; i < 4; i++) { 
        printf("ID: %d\n", produtos[i].id); 
        printf("Nome: %s\n", produtos[i].nome);
        printf("Preço: %.2f\n", (float)produtos[i].preco / 100); // Imprime preço com duas casas decimais
        printf("Quantidade: %d\n", produtos[i].quantidade);
        printf("\n"); 
    }

    return 0;
}