print("Quabtidade de tinta para pinta a sua parede")
altura = float(input("Digite a altura da parede: "))
largura = float(input("Digite a largura da parede: "))

area_total = altura * largura
tinta = area_total / 2

print(f"Você vai precisar de {tinta:.2f} litros de tinta para pintas a sua parede.")