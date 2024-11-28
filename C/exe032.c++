#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");
    int i;
    int soma = 0;
    
    for (i = 0; i <= 100; i ++) {
            if (i % 5 == 0) {//verefica se o resto é igual a 0.
            printf("%d\n", i);
                soma = soma + i;    
            }        
    }
printf("O valor da soma é %d\n", soma);
    return 0;
}