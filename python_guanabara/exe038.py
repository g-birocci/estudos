velo = float(input("Digite a velociade do carro km/h: "))

multa = (velo - 80) * 7

if velo <= 80.0:
    print("Velocidade dentro do limite!")
else:
    print(f"Sua velocidade é {velo}, está acima do permitido e o valor da multa é: £{multa}")