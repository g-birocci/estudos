sair = True
contador = soma = 0
maior = menor = None
while sair:
    num = int(input("Digite um numero: "))
    soma += num
    contador += 1
    media = (soma / contador)

    if contador == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
            
    stop = str(input("VC quer continuar [S/N] ? ")).upper().strip()
    if stop == "S":
        sair = True
    else:
        print(f"A média de todos os valores são {media}.")
        print(f"O maior numero inserido é {maior}.")
        print(f"O menor valor inserido foi {menor}.")
        sair = False
