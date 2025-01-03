name = (input("Digite algo pra ver se é um palíndromo: ")).strip().upper()
name_junto = name.split()
junto = "".join(name_junto)
inverso = ""
for letra in range (len(junto) -1, -1, -1):
    inverso += junto[letra]

if inverso == junto:
    print("Esta frase é um palindromo.")
else:
    print("Está frase não é palindromo.")
