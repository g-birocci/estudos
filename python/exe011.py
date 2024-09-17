n = int(input("digite a quantidade de nota desejada: "))
notas = 0
nota = 0
for i in range(n):
    isValid = False
    while isValid == False:
        nota = float(input("Digite a nota: "))
        if nota >= 0 and nota <= 20: 
            notas += nota
            isValid = True
        else:  
            print("Nota errada.")
media = notas/n
print(media)        