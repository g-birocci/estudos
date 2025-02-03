while True:
    print("-" * 25)
    n = int(input("Digite a o numero da tabuada que vc deseja: "))
    print("-" * 25)
    if n < 1:
        print("Programa encessado.")
        break
    for i in range (11):
        x = n * i
        print(f"{n} X {i} = {x}")
