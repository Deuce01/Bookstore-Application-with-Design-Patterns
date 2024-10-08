# **Bookstore Application with Design Patterns** 📚

This project is a simple **Bookstore Management Application** that demonstrates the use of several **design patterns** in Python:

1. **MVC (Model-View-Controller)**
2. **Singleton**
3. **Factory**

The application allows users to add books (categorized as Fiction or Non-Fiction) and view the list of added books. The patterns used make the codebase more modular, maintainable, and scalable.

---

## **Features**

- **Book Management**: Add and view books by category (Fiction, Non-Fiction).
- **Logger (Singleton)**: A global logger instance to log book additions.
- **Book Factory**: Creates different types of books using the **Factory Pattern**.
- **MVC Architecture**: Separation of concerns between data (Model), user interface (View), and control logic (Controller).

---

## **Technologies Used**

- **Python** 🐍
  - **Singleton Pattern**: Used to create a global logger instance.
  - **Factory Pattern**: Used to create different types of books (Fiction, Non-Fiction).
  - **MVC Pattern**: For organizing code structure, separating Model, View, and Controller.

---

## **Project Structure**

```plaintext
bookstore/
│
├── main.py                # Entry point of the application
├── model.py               # Model to manage book data
├── view.py                # View to display books and take user input
├── controller.py          # Controller to manage user interaction
├── logger.py              # Singleton Logger class
├── book_factory.py        # Factory for creating Fiction/Non-Fiction books
└── logs/                  # Directory for log files
```

---

## **How It Works**

### **1. Add Books**
You can add books to the store by choosing their category (**Fiction** or **Non-Fiction**) and providing a title.

### **2. View Books**
After adding books, you can view the entire list of added books.

### **3. Logging**
Each time you add a book, a log entry is created in `logs/bookstore_log.txt` using a **Singleton Logger**.

---

## **Getting Started**

### **1. Clone the repository**:



### **2. Navigate to the project directory**:

```bash
cd bookstore
```

### **3. Run the application**:

```bash
python main.py
```

---

## **Design Patterns Breakdown**

### **1. Singleton Pattern**

Used in `logger.py` to ensure that only one instance of the `Logger` class is created. All logs are written to `logs/bookstore_log.txt` by this single instance.

### **2. Factory Pattern**

The `BookFactory` class in `book_factory.py` creates different types of books (Fiction, Non-Fiction) based on user input.

### **3. MVC Pattern**

- **Model**: `BookModel` in `model.py` manages book data.
- **View**: `BookView` in `view.py` handles displaying and receiving data from the user.
- **Controller**: `BookController` in `controller.py` coordinates user actions and updates the Model and View accordingly.

---

## **Example Usage**

1. **Add a Book**:
    - You will be prompted to input the book category (Fiction/Non-Fiction) and the book title.
  
2. **View Books**:
    - Lists all the books you've added to the store, displaying their title and category.

3. **Logging**:
    - Check the `logs/bookstore_log.txt` file to see the logs of all the books you've added.

---

## **Future Improvements**

- Implement book removal functionality.
- Add support for additional book categories.
- Integrate a graphical user interface (GUI) for better user interaction.

---

## **Contributing**

Feel free to contribute by opening an issue or submitting a pull request. For major changes, please discuss them in an issue first to ensure alignment.

---

## **License**

This project is licensed under the MIT License.

---

**Enjoy managing your bookstore!** 📖🎉
