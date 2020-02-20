from hashcode.model.book import Book
from typing import List


class Library:
    def __init__(self, books: List[Book], sign_time: int, books_per_day: int, id: int):
        self.id = id
        self.books = set(books)
        self.sign_time = sign_time
        self.books_per_day = books_per_day
