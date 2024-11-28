#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

int main() {
    char a;
    a = 97;
    char A;
    A = 65;

    for (a = 97; a <= 122; a++) {
        printf("%c ", a);
    }
    
    for (A = 65; A <= 90 ; A++) {
        printf("%c ", A);
    }
    return 0;
}