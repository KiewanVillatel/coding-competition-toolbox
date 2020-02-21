class Library:
    def __init__(self, books, sign_time: int, books_per_day: int, id: int):
        self.id = id
        self.books = []
        for b in books:
            self.books.append(b)
        self.sign_time = sign_time
        self.books_per_day = books_per_day
        self.sort_books()

    def remove_book(self, book):
        self.books.remove(book)
        self.need_sort = True

    def sort_books(self):
        self.books.sort(key=lambda b: b.score, reverse=True)
        self.need_sort = False

    def get_score(self, remaining_timesteps):
        if self.need_sort:
            self.sort_books()
        return sum([b.score for b in self.books[:remaining_timesteps - self.sign_time]])
