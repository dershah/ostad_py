class Book:
    def __init__(self, title, author, isbn):
        self.title= title
        self.author = author
        self.isbn = isbn
        self.available = True

    def display_book(self):
        return f"ISBN: {self.isbn}  Title: {self.title}  Author: {self.author}  Status: {self.available}"
    # Use encapsulation for available.
    # Create
    # Getter
    # Setter