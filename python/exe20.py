cores = {"vermelho": "red", "azul": "blue", "verde": "green", "amarelo": "yellow", "preto": "black"}
print("Bem-vindo ao tradutor de cores <3 ")
cor = input("Digite a cor que deseja traduzir: ").lower()
if cor in cores:
    print("A cor " + cor + " em ingles é " + cores[cor] + ".")
else:
    print("Não é possivel traduzir essa cor.")
