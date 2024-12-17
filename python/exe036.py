'''
Exercício 5: Falsy Truthy

Crie um programa que verifique se uma variável é Falsy ou Truthy. Teste o programa com os valores 0, 1, "" e "Python".
'''

def check_f_t(var):
    if (var == "" or var == None or var == '0'):
        print("Falsy")
    else:
        print("Truthy")

var = input("Digite algo: ")
check_f_t(var)