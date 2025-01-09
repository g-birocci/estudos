#include <stdio.h>
#include <locale.h>


int calcula_ordenado(int tipo_funcionario); 

int main() {
    setlocale(LC_ALL, "Portuguese");

    int tipo_funcionario; 

    printf("Digite o tipo do funcionario: ");
    scanf("%d", &tipo_funcionario); 

    float ordenado = calcula_ordenado(tipo_funcionario); 

    if (ordenado != -1) { 
        printf("O valor do ordenado é: %.2f\n", ordenado); 
    } else {
        printf("Não existe esse tipo de funcionario.\n");
    }

    return 0;
}

int calcula_ordenado(int tipo_funcionario) {
    float ordenado;

    switch (tipo_funcionario) {
        case 1:
            ordenado = (1000 - (1000 * 0.05)); 
            break;
        case 2:
            ordenado = (1200 - (1000 * 0.06));
            break;
        case 3:
            ordenado = (1500 - (1000 * 0.07));
            break;
        default:
            return -1;
    }

    return ordenado;
}