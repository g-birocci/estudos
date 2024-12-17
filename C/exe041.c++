#include <iostream>

using namespace std;

int main() {
    const int TAMANHO = 5;
    int matriz[TAMANHO][TAMANHO];
    int soma_linha;

    // Lendo os valores da matriz
    cout << "Digite os valores da matriz " << TAMANHO << "x" << TAMANHO << ":" << endl;
    for (int i = 0; i < TAMANHO; i++) {
        for (int j = 0; j < TAMANHO; j++) {
            cin >> matriz[i][j];
        }
    }

    // Imprimindo a matriz original e somando as linhas
    cout << "\nMatriz original e soma das linhas:\n";
    for (int i = 0; i < TAMANHO; i++) {
        soma_linha = 0;
        for (int j = 0; j < TAMANHO; j++) {
            cout << matriz[i][j] << " ";
            soma_linha += matriz[i][j];
        }
        cout << "  Soma da linha: " << soma_linha << endl;
    }

    // Imprimindo a matriz transposta
    cout << "\nMatriz transposta:\n";
    for (int i = 0; i < TAMANHO; i++) {
        for (int j = 0; j < TAMANHO; j++) {
            cout << matriz[j][i] << " ";
        }
        cout << endl;
    }

    return 0;
}