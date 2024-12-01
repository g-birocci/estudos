import random

num1 = str(input("Digite o nome do primeiro aluno: "))
num2 = str(input("Digite o nome do segundo aluno: "))
num3 = str(input("Digite o nome do terceiro aluno: "))
num4 = str(input("Digite o nome do quarto aluno: "))

lista = [num1, num2, num3, num4]
random.shuffle(lista)

print("A ordem de apresentação será... ")
print(lista)