#include <stdio.h>
#include <locale.h>


int calcula_ordenado(int tipo_funcionario); 

int main() {
    setlocale(LC_ALL, "Portuguese");


    int n1 = 100;
    int *ptr = &n1;


    printf("%d\n", n1);
    printf("%p", (void*)&n1);

    return 0;
}
