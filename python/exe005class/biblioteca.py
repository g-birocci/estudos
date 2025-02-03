import json

class Books:
    def __init__(self, title, author, year, genres = list):
        self.title = title
        self.author = author
        self.year = year
        self.genres = genres
        
        
    def serializar(book_list, json_file_book):

        livros = [book.__dict__ for book in book_list]
        with open(json_file_book, "w", encoding = "utf-8") as arquivo:
            json.dump(livros, arquivo, indent = 4)

