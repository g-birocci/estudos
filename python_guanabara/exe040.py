km = float(input("Digite a distância da sua viagem: "))

if km <= 200:
    p = km * 0.50
    print(f"O custo da sua viagem será de £{p:.2f}")
else:
    p = km * 0.45
    print(f"O custo da sua viagem será de £{p:.2f}")