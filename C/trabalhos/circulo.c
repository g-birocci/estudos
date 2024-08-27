/******************************************************************************

                            Online C Compiler.
                Code, Compile, Run and Debug C program online.
Write your code in this editor and press "Run" button to compile and execute it.

*******************************************************************************/

#include <stdio.h>
#define PI 3.14159265

int main()
{
    float raio;
    double area, comprimento;
    printf ("Digite o raio do circulo:\n        cm\r");
    scanf ("%f", &raio);
    area = (raio*raio)*PI;
    comprimento = raio*2*PI;
    system ("cls");
    printf ("A area do seu circulo e: %.2f cm\n", area);
    printf ("O comprimento do seu circulo e: %.2f cm", comprimento);
    printf ("\n\n");
    system ("pause");
}