tuplas = ()
cont = 0
par = 0
for num in range(4):
    num = int(input("Digite um numero: "))
    if num == 9: #vereficar quantos 9 foram digitados
        cont += 1

    if num % 2 == 0: #verefica qauntos numeros paares foram digitados.
        par += 1

    tuplas += (num, ) #tupla é imutavel, mas vc pode fazer uma tupla pra receber outras tuplas.

print(f"Você digitou os valores {tuplas}")
print(f"O numero 9 apareceu {cont} vezes")

if 3 in tuplas:  # Verifica se o número 3 está na tupla
    print(f"O valor 3 está na posição {tuplas.index(3)}")
else:
    print("O número 3 não foi digitado.")
    
print(f"Foram digitados {par} numeros pares.")