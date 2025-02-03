tupla = ("agua", "suco", "coxinha", "torta")

# for cont in range(0, len(tupla)):
#  print(f"Eu vou comer {tupla[cont]}")

#for comida in tupla:
 #   print(f"Eu vou comer {comida}")

for pos, comida in (tupla):
    print(f"Eu vou comer {tupla} na posição {pos}.") #enumerate mostra a posição.

print("Acabou")

a = (2,5,3)
b = (6,3,2)
c = a + b
print(c)