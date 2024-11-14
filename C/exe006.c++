#include <stdio.h>
#include <stdlib.h>
#include <locale.h>
#include <iostream>
using namespace std;
int main ()
{
    setlocale(LC_ALL,"Portuguese");
    int num1;
    int num2;
    float resul;
    int op;

    cout << "Digite o segundo numero: ";
    cin >> num1;
    
    cout << "Digite o segundo numero: ";
    cin >> num2;
    
    cout << "Qual operação deseja fazer soma [1], subtração [2], multiplicação[3] ou divisão 4: ";
    cin >> op;
    
    if (op == 1) {
    resul = num1 + num2;
    cout << resul;
    }
    
    if (op == 2) {
    resul = num1 - num2;
    cout << resul;
    }
    
    if (op == 3) {
    resul = num1 * num2;
    cout << resul;
    }
    
    if (op == 4) {
        if (num1 and num2 > 0) { 
            resul = num1 / (float)num2; // quando vc tem um var int na saida nunca vai ser flout, por isso vc declado no resultado pra ter uma saida em flout.
            cout << resul;
            }
        else {
            cout << "Deixa de ser burro!!!";
        }
    }
    
    return 0;
}