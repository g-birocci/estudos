#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int x = 10;
    int y = 20;
    int *ptr = &x;
    int *ptr1 = &y;
    
    *ptr = 100;
    *ptr1 = 200;

    printf("O novo valor de x: %d \n", x);
    printf("O novo valor de y: %d", y);



    return 0;
}
