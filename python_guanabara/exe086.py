times_brasileirao_2015 = (
    "Corinthians", "Atlético-MG", "Grêmio", "São Paulo", "Internacional", 
    "Sport", "Santos", "Cruzeiro", "Palmeiras", "Ponte Preta", 
    "Flamengo", "Fluminense", "Chapecoense", "Atlético-PR", "Coritiba", 
    "Figueirense", "Joinville", "Goiás", "Vasco da Gama", "Avaí"
)

print(f"Os 5 primeiros colocado do brasileiro foi {times_brasileirao_2015[:5]}")
print(f"Os 4 ultimos colocados foram {times_brasileirao_2015[-4:]}")
print(f"Os times em ordem alfabetica {sorted(times_brasileirao_2015)}") #coloca em ordem

for cont, time in enumerate(times_brasileirao_2015): #enumera a tupla
    print(f"{cont} - {time}")

print(f"O time da chapecoence está na {times_brasileirao_2015.index("Chapecoense") + 1}ª lugar.")