class Book:
    def __init__(self, title, category):
        self.title = title
        self.category = category

class FictionBook(Book):
    def __init__(self, title):
        super().__init__(title, "Fiction")

class NonFictionBook(Book):
    def __init__(self, title):
        super().__init__(title, "Non-Fiction")

class BookFactory:
    @staticmethod
    def create_book(book_type, title):
        if book_type == 'Fiction':
            return FictionBook(title)
        elif book_type == 'Non-Fiction':
            return NonFictionBook(title)
        else:
            return None
