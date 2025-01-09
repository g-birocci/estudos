#include <stdio.h>
#include <locale.h>

int main() {
    setlocale(LC_ALL, "Portuguese");

    int m = 29;
    int *ab;
    
    
    printf("%p\n", &m);
    printf("%d\n", m);

    ab = &m;
    
    printf("%d\n", m);

    m = 34;
    
    printf("%d\n", m);
    printf("%p\n", &m);

    *ab = 7;

    printf("%d", m);

    return 0;
}