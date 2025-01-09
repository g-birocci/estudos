#include <stdio.h>
#include <locale.h>
 
int main() {
    setlocale(LC_ALL, "Portuguese");

    float n1;
    float n2;
    float n3;
    float media;

    printf("Digite o primeiro valor: ");
    scanf("%f", &n1);

    printf("Digite o segundo valor: ");
    scanf("%f", &n2);

    printf("Digite o segundo valor: ");
    scanf("%f", &n3);

    media = (n1 + n2 + n3)/3;

    if (media > 100) {
        printf("Objetivo ultrapassado. a média foi %.1f", media);
    } else if (media == 100) {
        printf("Objetivo atingido. a media foi %.1f", media);
    } else {
        printf("Objetivo não atingido, a media foi %.1f", media);
    }
    

    return 0;
}