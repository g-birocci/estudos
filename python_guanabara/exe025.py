import random

import random
num1 = input("Digite o nome do primeiro aluno: ")
num2 = input("Digite o nome do segundo aluno:")
num3 = input("Digite o nome do terceiro aluno: ")
num4 = input("Digite o nome do quarto aluno: ")

aluno_sorteado = random.shuffle(1, 4)

print(aluno_sorteado)