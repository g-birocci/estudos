#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <iostream>
using namespace std;

int main () {
    setlocale(LC_ALL,"Portuguese");

    int id;
    float valor_horas;
    float falta;
    float dia_falta;
    int mes = 176;
    float salario;

    printf ("Digite o seu id: ");
    scanf("%i", &id);

    printf ("Digite quantas horas faltou: ");
    scanf ("%f", &falta);
    
    printf("Digite o valor da sua horas trabalhada: ");
    scanf("%f", &valor_horas);

    printf("O id é: %i\n", id);

    dia_falta = (mes - falta) / 8;
    printf("O total de falta foi: %.2f\n",dia_falta);

    salario = (mes - falta) * valor_horas;
    printf("O valor do sálario é £%.2f\n", salario);


    return 0;
}