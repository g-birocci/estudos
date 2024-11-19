#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <iostream>
using namespace std;

int main() {
    setlocale(LC_ALL, "Portuguese");

    int i = 1, num;
    while (i < 6)
    {
        printf("%d", i);
        i++;
    }
    

    return 0;
}
