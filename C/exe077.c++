#include <stdio.h>
#include <stdlib.h>
#include <locale>


int main() {
    setlocale(LC_ALL, "Portuguese");

    int fgetc("ficheiro_c.txt");

    while ((fgetc(file)) !=EOF)
    {
        putchar(ch);
    }
    

    return 0;
}