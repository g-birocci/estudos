import json

class Movie:
    def __init__(self, title, author, year, genres):
        self.title = title
        self.author = author
        self.year = year
        self.genres = genres

    def __repr__(self):
        return f"Movie(title='{self.title}', author='{self.author}', year={self.year}, genres={self.genres})"

class Filmes:
    def deserializar(self, arquivo_json):
        with open(arquivo_json, "r", encoding="utf-8") as file:
            filmes = json.load(file)

            lista_filmes = []
            for item in filmes:
                title = item.get('title')
                author = item.get('director')  # Corrigido para usar 'director'
                year = item.get('year')
                genres = item.get('genres')  # Corrigido para usar 'genres'

                lista_filmes.append(Movie(title, author, year, genres))

            return lista_filmes

    