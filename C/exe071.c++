#include <stdio.h>
#include <locale.h>

enum cor {vermelho, verde, azul, amarelo};

int main () {
    
    int carro = vermelho;
    int barco = azul;

    printf("O primeiro carro tem a cor %d\n", carro);
    printf("O primeiro barco tem a cor %d", barco);

    return 0;
}