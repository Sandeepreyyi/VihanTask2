class Book:
    def __init__(self, title, author, isbn, genre, quantity):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.genre = genre
        self.quantity = quantity

    def update_info(self, title=None, author=None, genre=None, quantity=None):
        if title:
            self.title = title
        if author:
            self.author = author
        if genre:
            self.genre = genre
        if quantity is not None:
            self.quantity = quantity


class Borrower:
    def __init__(self, name, contact_details, membership_id):
        self.name = name
        self.contact_details = contact_details
        self.membership_id = membership_id

    def update_info(self, name=None, contact_details=None):
        if name:
            self.name = name
        if contact_details:
            self.contact_details = contact_details


class Library:
    def __init__(self):
        self.books = {}
        self.borrowers = {}
        self.borrowed_books = {}

    def add_book(self, title, author, isbn, genre, quantity):
        if isbn in self.books:
            self.books[isbn].update_info(quantity=self.books[isbn].quantity + quantity)
        else:
            self.books[isbn] = Book(title, author, isbn, genre, quantity)

    def update_book(self, isbn, title=None, author=None, genre=None, quantity=None):
        if isbn in self.books:
            self.books[isbn].update_info(title, author, genre, quantity)

    def remove_book(self, isbn):
        if isbn in self.books:
            del self.books[isbn]

    def add_borrower(self, name, contact_details, membership_id):
        self.borrowers[membership_id] = Borrower(name, contact_details, membership_id)

    def update_borrower(self, membership_id, name=None, contact_details=None):
        if membership_id in self.borrowers:
            self.borrowers[membership_id].update_info(name, contact_details)

    def remove_borrower(self, membership_id):
        if membership_id in self.borrowers:
            del self.borrowers[membership_id]

    def borrow_book(self, membership_id, isbn, due_date):
        if membership_id in self.borrowers and isbn in self.books and self.books[isbn].quantity > 0:
            self.books[isbn].quantity -= 1
            self.borrowed_books[(membership_id, isbn)] = due_date

    def return_book(self, membership_id, isbn):
        if (membership_id, isbn) in self.borrowed_books:
            del self.borrowed_books[(membership_id, isbn)]
            self.books[isbn].quantity += 1

    def search_books(self, title=None, author=None, genre=None):
        results = []
        for book in self.books.values():
            if (title and title.lower() in book.title.lower()) or \
               (author and author.lower() in book.author.lower()) or \
               (genre and genre.lower() in book.genre.lower()):
                results.append((book.title, book.author, book.genre, book.quantity))
        return results

    def book_availability(self, isbn):
        if isbn in self.books:
            return self.books[isbn].quantity
        return 0

# Example usage:
library = Library()
library.add_book("The Great Gatsby", "F. Scott Fitzgerald", "1234567890", "Fiction", 5)
library.add_borrower("John Doe", "john.doe@example.com", "M001")
library.borrow_book("M001", "1234567890", "2024-07-01")
print(library.search_books(author="F. Scott Fitzgerald"))
print("Availability of 'The Great Gatsby':", library.book_availability("1234567890"))
library.return_book("M001", "1234567890")
print("Availability of 'The Great Gatsby' after return:", library.book_availability("1234567890"))
