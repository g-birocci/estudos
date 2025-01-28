while True:
    print("-"*30)
    n = int(input("Digite a o numero da tabuada que vc deseja: "))
    print("-"*30)
    if n < 1:
        print("Programa encessado.")
        break
    for i in range (11):
        x = n * i
        print(f"{n} X {i} = {x}")
