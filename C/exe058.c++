#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int m = 10;
    int n, o;
    int *z;

    z = &m;

    printf("%d", *z); 
    printf("%d\n", z);
    printf("%d\n", &m);
    printf("%d\n", &n);
    printf("%d", &o);



    return 0;
}

    