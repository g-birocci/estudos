#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    float tem_max[5];
    float tem_min[5];
    float tem_media[5];

    printf("Digite as temperaturas máximas e mínimas:\n");
    for (int i = 0; i < 5; i++) {
        printf("Cidade %d:\n", i+1);
        printf("Temperatura máxima: ");
        scanf("%f", &tem_max[i]);
        printf("Temperatura mínima: ");
        scanf("%f", &tem_min[i]);
    }

    
for (int i = 0; i < 5; i++) {
    tem_media[i] = (tem_max[i] + tem_min[i]) / 2;
}

printf("\nMédias das temperaturas:\n");
for (int i = 0; i < 5; i++) {
    printf("Local %d: %.2f\n", i+1, tem_media[i]);
}

    return 0;
}