#include <stdio.h>
#include <stdlib.h>

int main() {
    int *prt_vetor;
    int espacodovetor = 10000000000000;

    prt_vetor = (int *)malloc(espacodovetor * sizeof(int));
    
    if (prt_vetor == NULL) {
        printf("Falha na alocação, não tem memória sufciente");
        return 1;
    } else {
        printf("Memória alocada");
    }

    free(prt_vetor);

    return 0;
}

//A memória estática ela tem que ser difinida antes do programa seja exectado e quando o programa termina de compilar ele libera o espaço pra outro programa poder usar aquele espaço.
//A memória dimanica ela pode ser definida definida durante a execução do programa e pra fazer isso utiliza a função malloc, calloc, realloc, e tambem temos que usar o free pra liberar a memória que pode ter alto risco de erros como vazamentos.
