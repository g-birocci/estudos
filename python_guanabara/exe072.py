first = int(input("Digite o primeiro elemento: "))
razao = int(input("Razão: "))
n = int(input("Quantos elemento você quer exibir: "))
pa = []
contador = 0
termo = first
while contador < n:
    pa.append(termo)
    termo += razao
    contador += 1

print("Os primeiros", n, "elementos da PA são:", pa)