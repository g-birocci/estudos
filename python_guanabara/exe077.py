soma = 0
while True:
    n = int(input("Digite um numero: (999 pra parar): "))
    if n == 999:
        print(f"A soma do valores é {soma}")
        break
    soma = soma + n
    
    