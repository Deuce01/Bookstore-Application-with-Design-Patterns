from controller import BookController

if __name__ == "__main__":
    controller = BookController()

    while True:
        action = input("Choose action: (1) Add book, (2) Show books, (3) Exit: ")

        if action == "1":
            controller.add_book()
        elif action == "2":
            controller.show_books()
        elif action == "3":
            break
        else:
            print("Invalid choice.")
