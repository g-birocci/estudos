n1 = int(input("Digite um numero: "))
u = n1 // 1 % 10
d = n1 // 10 % 10
c = n1 // 100 % 10
m = n1 // 1000 % 10

print(f"Unidade: {u}")
print(f"Desena: {d}")
print(f"Centena: {c}")
print(f"Milhar: {m}")