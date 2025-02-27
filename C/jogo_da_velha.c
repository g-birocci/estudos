#include <stdio.h>
#include <stdlib.h>
#include <time.h>

char tabuleiro[3][3];
const char JOGADOR = 'X';
const char COMPUTADOR = 'O';

void resetarTabuleiro() {
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            tabuleiro[i][j] = ' ';
        }
    }
}

void imprimirTabuleiro() {
    printf("\n");
    printf(" %c | %c | %c \n", tabuleiro[0][0], tabuleiro[0][1], tabuleiro[0][2]);
    printf("---|---|---\n");
    printf(" %c | %c | %c \n", tabuleiro[1][0], tabuleiro[1][1], tabuleiro[1][2]);
    printf("---|---|---\n");
    printf(" %c | %c | %c \n", tabuleiro[2][0], tabuleiro[2][1], tabuleiro[2][2]);
    printf("\n");
}

int verificarEspacosVazios() {
    int espacosVazios = 9;
    for(int i = 0; i < 3; i++) {
        for(int j = 0; j < 3; j++) {
            if(tabuleiro[i][j] != ' ') {
                espacosVazios--;
            }
        }
    }
    return espacosVazios;
}

void jogadaComputador() {
    srand(time(0));
    int x, y;
    
    do {
        x = rand() % 3;
        y = rand() % 3;
    } while(tabuleiro[x][y] != ' ');
    
    tabuleiro[x][y] = COMPUTADOR;
}

int verificarVencedor(char jogador) {
    // Verificar linhas
    for(int i = 0; i < 3; i++) {
        if(tabuleiro[i][0] == jogador && tabuleiro[i][1] == jogador && tabuleiro[i][2] == jogador)
            return 1;
    }
    // Verificar colunas
    for(int j = 0; j < 3; j++) {
        if(tabuleiro[0][j] == jogador && tabuleiro[1][j] == jogador && tabuleiro[2][j] == jogador)
            return 1;
    }
    // Verificar diagonais
    if(tabuleiro[0][0] == jogador && tabuleiro[1][1] == jogador && tabuleiro[2][2] == jogador)
        return 1;
    if(tabuleiro[0][2] == jogador && tabuleiro[1][1] == jogador && tabuleiro[2][0] == jogador)
        return 1;
    
    return 0;
}

void jogadaUsuario(char *nome) {
    int pos;
    do {
        printf("%s, escolha uma posicao (1-9): ", nome);
        scanf("%d", &pos);
        pos--;

        int x = pos / 3;
        int y = pos % 3;

        if(pos < 0 || pos > 8 || tabuleiro[x][y] != ' ') {
            printf("Posicao invalida!\n");
        } else {
            tabuleiro[x][y] = JOGADOR;
            break;
        }
    } while(1);
}

int main() {
    char nomeJogador[50];
    printf("Digite seu nome: ");
    scanf("%s", nomeJogador);
    printf("\nBem-vindo ao Jogo da Velha, %s!\n", nomeJogador);
    printf("Voce e' X. O computador e' O.\n");
    printf("As posicoes sao numeradas de 1 a 9, da esquerda para direita, de cima para baixo.\n");

    resetarTabuleiro();

    while(1) {
        imprimirTabuleiro();
        jogadaUsuario(nomeJogador);
        
        if(verificarVencedor(JOGADOR)) {
            imprimirTabuleiro();
            printf("Parabens %s! Voce venceu!\n", nomeJogador);
            break;
        }
        
        if(verificarEspacosVazios() == 0) {
            imprimirTabuleiro();
            printf("Empate!\n");
            break;
        }

        jogadaComputador();
        
        if(verificarVencedor(COMPUTADOR)) {
            imprimirTabuleiro();
            printf("O computador venceu!\n");
            break;
        }
        
        if(verificarEspacosVazios() == 0) {
            imprimirTabuleiro();
            printf("Empate!\n");
            break;
        }
    }

    return 0;
}