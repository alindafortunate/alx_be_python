class Book:

    def __init__(self, title, author, is_checked_out=True):
        self.title = title
        self.author = author
        self._is_checked_out = is_checked_out

    def return_book(self):
        return f"{self.title} by {self.author}"


class Library(Book):
    def __init__(self):
        self._books = []

    def add_book(self, book):
        self._books.append(book)

    def check_out_book(self, title):
        try:
            for book in self._books:
                if book.title == title:
                    book._is_checked_out = False
        except ValueError:
            print(f"The book doesn't exist.")

    def return_book(self, title):
        try:
            for book in self._books:
                if book.title == title:
                    book._is_checked_out = True
        except ValueError:
            print(f"The book doesn't exist")

    def list_available_books(self):
        for book in self._books:
            if book._is_checked_out == True:
                print(f"{book.title} by {book.author}")
