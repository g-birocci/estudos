palabras = ("computador", "programação", "tecnologia", "desenvolvimento", "redes", "internet", "dados", "seguranca", "codigo", "hardware", "software", "inteligência", "aprendizado", "automatizacao", "algoritmo")

for palavra in palabras:
    print(f"Na palavra {palavra.lower()} temos ", end='')
    for letra in palavra:
        if letra.lower() in "aeiou":
            print(letra, end='')
    print()