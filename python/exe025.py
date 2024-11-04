def contar(word):  
    vogais = ["a","e","i","o","u"]
    contador = 0

    for letra in word:
        if letra in vogais:
            contador = contador + 1
    return contador

word =input("Digite uma palavra: ").lower()
print(contar(word))
