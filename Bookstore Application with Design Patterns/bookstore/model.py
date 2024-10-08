from logger import Logger

class BookModel:
    def __init__(self):
        self.books = []
        self.logger = Logger()

    def add_book(self, book):
        self.books.append(book)
        self.logger.log(f"Added book: {book.title}, Category: {book.category}")

    def get_books(self):
        return self.books
