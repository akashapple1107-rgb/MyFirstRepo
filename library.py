class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append(book_name)
        print(f"Book '{book_name}' added successfully.")

    def show_books(self):
        print("Books in Library:")
        for book in self.books:
            print("-", book)


# Main program
library = Library()
library.add_book("Software Engineering")
library.add_book("Data Structures")
library.show_books()