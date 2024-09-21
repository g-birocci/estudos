#include <stdio.h>
#include <math.h>

int main(){

    int contador = 1;
    int resul, numero;
    int mylist[10];
    int x = 0;

    printf("Qual tabuada vc deseja?: ");
    scanf("%d", &numero);
    while (contador <= 10){
        resul = (numero * contador);
        mylist[x] = resul;
        x++;
        contador++;
    }
    x=0;
    while (x < 10)
    {
        printf("%d\n", mylist[x]);
        x++;
    }
    
    return 0;
}
