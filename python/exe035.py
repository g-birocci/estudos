'''
Exercício 1: Comparação em Cadeia

Escreva um programa que verifique se um número está entre 10 e 20 (inclusive) utilizando comparação em cadeia.
'''
def check_num(numero):
    if numero >= 10 and numero <= 20:
        print("Este numero está entre 10 e 20.")
    else:
        print("O numero não está entre 10 e 20.")

numero = int(input("Insira um número: "))
check_num(numero)