#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main ()
{
    setlocale(LC_ALL,"Portuguese");
    printf("Hello Word!");
    system("PAUSE");

    return 0;
}