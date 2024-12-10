print("------ Formar Triângulo ------")
n1 = int(input("Digite um valor inteiro: "))
n2 = int(input("Digite um segundo valor: "))
n3 = int(input("Digite um terceiro valor: "))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print("--- Estes valores formam um triângulo. ---")
else:
    print("--- Não é possivel fazer um triângulo ---")