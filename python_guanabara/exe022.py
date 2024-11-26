import math
cateto1 = float(input("Digite o valor do cateto: "))
cateto2 = float(input("Digite o valor do careto adjacente: "))

hipotenusa = math.sqrt(cateto1**2 + cateto2**2)
print(f"O valor da hipotenusa é {hipotenusa:.2f}.")

