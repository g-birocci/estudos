#include <stdio.h>
#include <stdlib.h>
#define MAX_BUS 10 

int park[MAX_BUS];  
int first;         
int last;
int num_bus;


void create() {
    last = -1;     
    first = 0;    
    num_bus = 0;
}

int is_full() {
    return num_bus == MAX_BUS;
}

int is_empty() {
    return num_bus == 0;   
}

void insert(int position) {
    if (is_full()) {
        printf("Estacionamento cheio! Não é possível adicionar mais ônibus.\n");
        return;
    }
    
    last++;  
    if (last >= MAX_BUS) { 
        last = 0;
    }
    
    park[last] = position; 
    num_bus++;  
    printf("Ônibus %d adicionado na posição %d.\n", position, last);
}


int remove_bus() {
    if (is_empty()) {
        printf("Estacionamento vazio\n");
        return -1; 
    }

    int valor = park[first]; 
    first++;                  
    num_bus--;               

    if (first >= MAX_BUS) {  
        first = 0;  
    }

    printf("Ônibus %d removido.\n", valor);
    return valor;
}

// Função principal
int main(int argc, char *argv[]) {
    int num;
    int fazer;
    create();
    do {
        printf("1 - Adicionar ônibus\n");
        printf("2 - Remover ônibus\n");
        printf("Escolha uma opção: ");
        scanf("%d", &num);
        
        if (num == 1) {
            int position;
            printf("Digite o número do ônibus para adicionar: ");
            scanf("%d", &position);
            insert(position);
        } else if (num == 2) {
            remove_bus();
        } else {
            printf("Opção inválida. Tente novamente.\n");
        }

        printf("Deseja continuar? (1-Sim / 0-Não): ");
        scanf("%d", &fazer);
    } while (fazer == 1);
    
    return 0;
}
