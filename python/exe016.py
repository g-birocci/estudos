print("Insira 7 numeros entre PAR e IMPAR.  ")
numeros = []
par = []
impar = []
for i in range(7):
    valores = int(input("Quais numeros?  "))
    numeros.append(valores)   
    if valores % 2 == 0:
        par.append(valores)      
    else:
        impar.append(valores)       
if len(par) > len(impar):
    print("mais Par!")
else:
    print("Mais Impar!")   
print(numeros)
print(par)
print(impar)