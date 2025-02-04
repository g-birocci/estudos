#include <stdio.h>
#include <stdlib.h>
#include <locale>


int main() {
    setlocale(LC_ALL, "Portuguese");

    FILE *file; //Vai ser o ponteiro pra o arquivo
    char filename[] = "caracter-a-caracte_txt";

    file = fopen(filename, "w"); //esse bloco verefica se vai criar corretamente o arquivo, (Sempre usar)
    if (file == NULL) {
        printf("Erro ao criar o arquivo");
        return 1;
    }

    char texto[] = "manipulação de ficheiros em C"; // isto faz com que seja escrito caracter por caracter no arquivo 
    for (int i = 0; texto[i] != '\0'; i++) {        // pode usar o fprint pra escrever direto.
        fputc(texto[i], file);
    }

    fclose(file);
    printf("Arquivo '%s'criado com sucesso. \n", filename);

    // está parte de cima foi criada para criar o arquivo e ver se está tudo ok    
    return 0;
}