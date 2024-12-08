frase = str(input("Digite uma frase: ")).lower().strip() #STRIP TIRA OS ESPAÇOS DO INICIO E FIM

print(frase.count("a"))

print(f"A letra foi encontrada na posição {frase.find("a") + 1}")