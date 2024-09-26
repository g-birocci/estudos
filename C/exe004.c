#include <stdio.h>
#include <stdlib.h>

int fila_park[10];  
int ultimo;         
int primeiro;       
int max;            
int num_bus;        

void create() {
    max = 10;        
    ultimo = -1;     
    primeiro = 0;    
    num_bus = 0;     
}

int is_full() {
    return num_bus == max;
}

int is_empty() {
    return num_bus == 0;   
}

void insert(int posi1) {
    if (is_full()) {
        printf("Estacionamento cheio! Não é possível adicionar mais ônibus.\n");
        return;
    }
    
    ultimo = (ultimo + 1) % max;  
    fila_park[ultimo] = posi1;   
    num_bus++;                   
    printf("Ônibus %d adicionado na posição %d.\n", posi1, ultimo + 1);
}

int main(int argc, char *argv[]) {
    int num;
    create();  // estacionamento
    
    printf("Digite o número do autocarro para adicionar: ");
    scanf("%d", &num);  
    insert(num);      
    
    return 0;
    system("pause");
}
