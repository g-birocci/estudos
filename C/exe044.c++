#include <stdio.h>
#include <locale.h>
 
double converter(double euros) {
    double taxa = 1.10;
    return euros * taxa;
}
 
int main() {
    setlocale(LC_ALL, "Portuguese");
 
    double euros, dolares;
 
    printf("Digite o valor em Euros: ");
    scanf("%lf", &euros);
 
    dolares = converter(euros);
 
    printf("%.2f Euros equivalem a %.2f Dolares.\n", euros, dolares);
 
    return 0;
}