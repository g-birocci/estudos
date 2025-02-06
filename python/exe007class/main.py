import os
from movie import Filmes

if __name__ == "__main__":
    caminho_atual = os.path.dirname(__file__)
    caminho_dados = os.path.join(caminho_atual, 'dados.json')

    filmes_obj = Filmes()
    dados_filmes = filmes_obj.deserializar(caminho_dados)

    for item in dados_filmes:
        print(f"Título: {item.title}, Autor: {item.author}, Ano: {item.year}, Gêneros: {', '.join(item.genres)}")
