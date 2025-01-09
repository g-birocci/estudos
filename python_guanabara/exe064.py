print("Bem-vindo")
menor = 0
maior = 0
for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}ª pessoa: "))
    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        elif peso < menor:
            menor = peso

print(f"O maior peso é: {maior}")
print(f"O menor peso é: {menor}")                                 
     
        
     
     