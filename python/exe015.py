print("Digite 5 Numeros")
lis_ta = []  
for i in range(5):
    valor = int(input("Digite o numero: "))
    lis_ta.append(valor)
print(sum(lis_ta))

lis_ta.sort(reverse=True)
print(lis_ta[0])
print(lis_ta[-1])
print(lis_ta)
