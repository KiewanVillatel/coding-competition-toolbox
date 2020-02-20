from hashcode.model.book import Book
# from heapq import heappush, heappop
from typing import List


class Library:
    def __init__(self, books: List[Book], sign_time: int, books_per_day: int, id: int):
        self.id = id
        self.books = []
        for b in books:
            self.books.heappush(b)
        self.sign_time = sign_time
        self.books_per_day = books_per_day
        self.compute_score()

    def get_score(self):
        return self.score

    def remove_book(self, book_scanned: Book):
        if book_scanned in self.books:
            self.books.remove(book_scanned)
            self.score -= self.score_per_book(book_scanned)

    def score_per_book(self, book: Book):
        return self.books_per_day * book.score / self.sign_time

    def compute_score(self):
        self.score = sum([self.score_per_book(b) for b in self.books])

    def update_score(self, books_scanned: List[Book]):
        for sb in books_scanned:
            if sb in self.book:
                self.score -= self.score_per_book(sb)
