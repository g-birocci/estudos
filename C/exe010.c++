#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <iostream>
using namespace std;

a + c, x + c,dx + x, ((int) dx) + ax, a + x, s + b, ax + b, s + c, ax + c, ax + ux, cujo conteúdo
inicial das variáveis é:
• int a = 125, b = 12345;
• long ax = 1234567890;
• short s = 4043;
• float x = 2.13459;
• double dx = 1.1415927;
• char c = 'W';
• unsigned long ux = 2541567890;

int main () {
    setlocale(LC_ALL,"Portuguese");
    
    printf("a + c: %d\n", a + c);              // int + char (char é convertido implicitamente para int)
    printf("x + c: %.5f\n", x + c);            // float + char (char é convertido implicitamente para float)
    printf("dx + x: %.7f\n", dx + x);          // double + float (float é promovido a double)
    printf("((int) dx) + ax: %d\n", (int) dx + ax); // casting de double para int + long
    printf("a + x: %.5f\n", a + x);            // int + float (int é promovido a float)
    printf("s + b: %d\n", s + b);              // short + int (short é promovido a int)
    printf("ax + b: %ld\n", ax + b);           // long + int
    printf("s + c: %d\n", s + c);              // short + char (char é promovido a int)
    printf("ax + c: %ld\n", ax + c);           // long + char (char é promovido a int)
    printf("ax + ux: %lu\n", ax + ux);         // long + unsigned long
    printf("\n");

    return 0;




}