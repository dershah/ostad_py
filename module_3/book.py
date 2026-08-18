class Book:
    def __init__(self, title, author, isbn):
        self._title = title
        self._author = author
        self._isbn = isbn
        self._available = 'available'

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, set_title):
        self._title = set_title

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, set_author): 
        self._author = set_author

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, set_isbn):
        self._isbn = set_isbn

    @property
    def available(self):
        return self._available

    @available.setter
    def available(self, set_available):
        self._available = set_available

    def display_book(self):
        return f"|- ISBN: {self._isbn} -|- Title: {self._title} -|- Author: {self._author} -|- Status: {self._available} -|\n"   