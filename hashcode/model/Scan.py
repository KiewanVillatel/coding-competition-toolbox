from hashcode.model.book import Book
from hashcode.model.library import Library
from typing import List


class Scan:
    def __init__(self, library: Library, books: List[Book]):
        self.library = library
        self.books = books
