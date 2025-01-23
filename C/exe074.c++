#include <stdio.h>
#include <locale.h>

enum meses {janeiro = 1, fevereiro = 2, marco = 3, abrir = 4, maio = 5, junho = 6, julho = 7, agosto = 8, setembro = 9, outubro = 10, novembro = 11, desembro = 12};

int main () {

    int mes_passado = fevereiro;

    printf("%d", mes_passado); 

    return 0;
}