print("Bem-vindo")
menor = 0
maior = 0
for i in range(0, 5):
    peso = float(input("Digite o seu peso: "))
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
     
        
     
     