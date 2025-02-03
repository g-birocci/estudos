#include <stdio.h>
#include <stdlib.h>
#include <locale>


int main() {
     setlocale(LC_ALL, "Portuguese");
     FILE *fp;
     fp = fopen("text.dat", "wb");
     if (fp == NULL)
        printf("Não foi possivel abrir o ficheiro");
    fclose(fp);

    return 0;
}