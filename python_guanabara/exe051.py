print("------ Formar Triângulo ------")
n1 = int(input("Digite um valor inteiro: "))
n2 = int(input("Digite um segundo valor: "))
n3 = int(input("Digite um terceiro valor: "))

if n1 + n2 > n3 and n1 + n3 > n2 and n2 + n3 > n1:
    print("--- Estes valores formam um triângulo. ---")
    if n1 == n2 and n2 == n3:
        print("--- Estes valores forma um triângulo equilátero ---")
    elif n1 == n2 or n2 == n3 or n1 == n3:
        print("Este triângulo é isóceles.")
    else:
        print("Este triângulo é escaleno.")
else:
    print("--- Não é possivel fazer um triângulo ---")