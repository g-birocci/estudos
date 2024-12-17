

def binario(n1):
        x = bin(n1)[2:]
        print(f"Este valor de {n1} em binario fica: {x}")

def octal(n1):
        x = oct(n1)[2:]
        print(f"Este valor de {n1} em octal fica : {x}")

def hexadecimal(n1):
        x = hex(n1)[2:]
        print(f"Este valor de {n1} em hexadecimal fica: {x}")

sair = True
while sair:
        n1 = int(input("Digite um numero pra converte: "))
        op = (input(''' Escolha a opsão desejada: 
                1 -- Para binário
                2 -- Para octal
                3 -- Para hexadecimal : '''))
        
    
        match op:
                case "1":
                        binario(n1)
                case "2":
                        octal(n1)
                case "3":
                        hexadecimal(n1)
                case "4":
                        print("Saiu do programa!")
                        sair = False
                case _:
                        print("Opção errada!!!")