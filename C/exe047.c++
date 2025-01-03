#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int numprimo (int n1) {
    if (n1 <= 1){
        return 0;
    }
    for (int i = 2; i <= n1 / 2; i++){
        if (n1 % i == 0){
            return 0;
        }
    }
    return 1;

}

int main() {
    setlocale(LC_ALL, "Portuguese");
    int n1;

    printf("Digite um valor pra vereficar se ele é um numero primo: ");
    scanf("%d", &n1);

    if (numprimo(n1)){
        printf("%d e um numero primo.", n1);
    }
    else {
        printf("%d nao é um numero primo.", n1);
    }
    return 0;
}