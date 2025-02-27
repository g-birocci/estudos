from menu import Menu
from coffee_maker import Cafeteira
from money_machine import MaquinaDinheiro

def main():
    menu = Menu()
    cafeteira = Cafeteira()
    caixa = MaquinaDinheiro()
    
    ligado = True
    while ligado:
        opcoes = menu.obter_itens()
        escolha = input(f"O que você gostaria? ({opcoes}): ").lower()
        
        if escolha == "off":
            print("Desligando a máquina...")
            ligado = False
        elif escolha == "relatorio":
            cafeteira.relatorio()
            caixa.relatorio()
        else:
            bebida = menu.encontrar_bebida(escolha)
            if bebida:
                if cafeteira.tem_recurso_suficiente(bebida) and caixa.realizar_pagamento(bebida.custo):
                    cafeteira.fazer_cafe(bebida)
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
