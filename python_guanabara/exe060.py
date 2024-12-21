first = int(input("Digite o primeiro elemento: "))
razao = int(input("Razão: "))
n = int(input("Quantos elemento você quer exibir: "))

last = first + (n - 1) * razao
last = last + 1

for pa in range(first, last, razao):
    print(pa)