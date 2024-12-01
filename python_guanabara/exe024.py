import random

num1 = input("Digite o nome do primeiro aluno: ")
num2 = input("Digite o nome do segundo aluno:")
num3 = input("Digite o nome do terceiro aluno: ")
num4 = input("Digite o nome do quarto aluno: ")

lista = [num1, num2, num3, num4]

aluno_sorteado = random.choice(lista)

print(aluno_sorteado)

# if aluno_sorteado == 1:
#     print(f"O alunno sorteado foi {num1}.")

# elif aluno_sorteado == 2:
#     print(f"O aluno sorteado foi {num2}.")

# elif aluno_sorteado == 3:
#     print(f"O aluno sorteado foi {num3}.")

# else: 
#     print(f"O aluno sorteado foi {num4}.")