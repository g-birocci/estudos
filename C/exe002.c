#include <stdio.h>
#include <stdlib.h>

/* run this program using the console pauser or add your own getch, system("pause") or input loop */

int pilha[30];
int pos;


void create(){
	
	pos =-1;
}
void push(int valor){
	pos = pos+1;
	pilha[pos]=valor;
	
	
}

int pop(){
	int valor;
	valor = pilha[pos];
	pos = pos-1;
	return valor;
}

int empty(){
	if (pos == -1){
		return 0;
	}else{
		return 1;
	}
}

int main(int argc, char *argv[]) {
	
	int varLer;
	int control=10;
	int resultado;
	create();
	printf("Digite o valor da tabuada:");
	scanf("%d",&varLer);
	while (control > 0){
		resultado = control*varLer;
		push(resultado);
		control = control -1;
		
	}

	while (empty() !=0){
	
		printf("%d\n",pop());
	}
	/**/
	system("pause");
	return 0;
}
