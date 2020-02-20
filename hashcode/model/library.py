from hashcode.model.book import Book
from typing import List


class Library:
    def __init__(self, books: List[Book], sign_time: int, books_per_day: int, id: int):
        self.id = id
        self.books = set(books)
        self.sign_time = sign_time
        self.books_per_day = books_per_day
        self.compute_score()

    def get_score(self):
        return self.score

    def update(self, books_scanned: List[Book]):
        for bc in books_scanned:
            if bc in self.books:
                self.books.remove(bc)
        self.compute_score()

    def compute_score(self):
        self.score = self.books_per_day * sum([b.score for b in self.books]) / self.sign_time
