class Library:
    def __init__(self, books, sign_time: int, books_per_day: int, id: int):
        self.id = id
        self.books = []
        for b in books:
            self.books.append(b)
        self.sign_time = sign_time
        self.books_per_day = books_per_day
        self.sum_score_books = sum([b.score for b in self.books])
        self.need_sort = False

    def remove_book(self, book):
        self.books.remove(book)
        self.sum_score_books -= book.score

    def get_score(self):
        return self.sum_score_books
