class BookView:
    def show_books(self, books):
        print("Book List:")
        for book in books:
            print(f"- {book.title} ({book.category})")

    def prompt_for_book(self):
        book_type = input("Enter book type (Fiction/Non-Fiction): ")
        title = input("Enter book title: ")
        return book_type, title
