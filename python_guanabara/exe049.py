print("---- Média do aluno ----")
n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira nota: "))

media = (n1+n2+n3)/3

if media < 5:
    print("Reprovado")
elif media < 6.9:
    print("Está de recuperação.")
else:
    print("Parabéns você passou de ano!")