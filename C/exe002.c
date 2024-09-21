#include <stdio.h>
#include <stdlib.h>

int main(){

    int contador = 1;
    int resul, numero;

    printf("Qual tabuada vc deseja?: ");
    scanf("%d", &numero);
    while (contador <= 10){
        resul = (numero * contador);
        printf("%d\n",resul);
        contador++;
    }
    return 0;
}