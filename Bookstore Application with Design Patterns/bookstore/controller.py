from model import BookModel
from view import BookView
from book_factory import BookFactory

class BookController:
    def __init__(self):
        self.model = BookModel()
        self.view = BookView()

    def add_book(self):
        book_type, title = self.view.prompt_for_book()
        book = BookFactory.create_book(book_type, title)
        if book:
            self.model.add_book(book)

    def show_books(self):
        books = self.model.get_books()
        self.view.show_books(books)
