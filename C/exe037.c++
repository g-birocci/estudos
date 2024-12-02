#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int np;

    printf("Quantas linha vc deseja ? ");
    scanf("%d", &np);

    for (int i = 1; i <= np; i++) {
        for (int n = 1; n <= i; n++) {
            printf("*");
        }
        printf("\n");    
    }
    return 0;
}
