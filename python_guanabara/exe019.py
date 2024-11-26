diaria = int(input("Quantos dias o carro foi alugado? "))
km = float(input("Quantos Km foi percorrido ? "))

pagar = (diaria * 60) + (km * 0.15)

print(f"O valor total a pagar é £{pagar}.")
