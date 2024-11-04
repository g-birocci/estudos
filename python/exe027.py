def countword(word):
    texto = word.split()
    num_palavras = {}

    for palavra in texto:
        if palavra in num_palavras:
            num_palavras[palavra] += 1
        else:
            num_palavras[palavra] = 1

    for palavra, quantidade in num_palavras.items():
        print(f"A palavra '{palavra}' aparece {quantidade} vezes.")

word = input("Digite um texto: ").lower()
countword(word)
