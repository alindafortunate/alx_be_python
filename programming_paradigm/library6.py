# Implement a Book class with public attributes title and author,
# and a private attribute _is_checked_out to track its availability.
# Implement a Library class with a private list _books to store instances of Book.
# Include methods to add_book, check_out_book(title), return_book(title), and list_available_books.

# Your Book class should provide methods to check a book out and return it, affecting its availability.
# Your Library class needs to manage a collection of books,
# including adding new books to the collection, checking a book out (which marks it as unavailable),
#  returning it (making it available again), and listing all available books.
# Implementing these functionalities requires careful thought about how objects
# interact with each other in terms of state and behavior.

# checked_out = False
# checked_out == False => False == False


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self._is_checked_out = False

    def check_book_out(self):
        if self._is_checked_out == False:
            self._is_checked_out = True

    def return_book(self):
        if self._is_checked_out == True:
            self._is_checked_out = False

    def is_available(self):
        return self._is_checked_out == False


class Library:
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if title == book.title:
                book.check_book_out()

    def return_book(self, title):
        for book in self._books:
            if title == book.title:
                book.return_book()

    def list_available_books(self):
        for book in self._books:
            if book.is_available() == True:
                print(f"{book.title} by {book.author}")
