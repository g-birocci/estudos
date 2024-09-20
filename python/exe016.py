print("Insira 7 numeros entre PAR e IMPAR.  ")
n = []
n_par = []
n_impar = []
for i in range(7):
    valores = int(input("Quais numeros?  "))
    n.append(valores)   
    if valores % 2 == 0:
        n_par.append(valores)      
    else:
        n_impar.append(valores)       
if len(n_par) > len(n_impar):
    print("mais Par!")
else:
    print("Mais Impar!")   
print(n)
print(n_par)
print(n_impar)