from biblioteca import Books

if __name__ == '__main__':
    book = Books(title= "Harry Potter", author="Bla - Bla", year = 1997, genres = ["Dystopian", "Political Fiction"])

    book1 = Books(title= "Harry Potter", author="Bla - Bla", year = 1997, genres = ["Dystopian", "Political Fiction"])

    book3 = Books(title= "Harry Potter", author="Bla - Bla", year = 1997, genres = ["Dystopian", "Political Fiction"])       

    book_list = [book, book1, book3]

    Books.serializar(book_list, "book_json")