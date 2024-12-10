ordenado = float(input("Digite o valor do seu ordenado: "))

if ordenado >= 1250:
    aumento = ordenado + (ordenado * 10)/100
    print(f"O valor do seu ordenado será de £{aumento:.2f}")
else:
    aumento = ordenado + (ordenado * 15)/100
    print(f"O valor do seu ordenado será de £{aumento:.2f}")