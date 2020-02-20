from __future__ import annotations
from hashcode.model.book import Book
from hashcode.model.library import Library
from typing import List



class Problem:

    def __init__(self, name: str, books: List[Book], libraries: List[Library], deadline: int):
        self.name = name
        self.books = books
        self.libraries = libraries
        self.deadline = deadline

    @staticmethod
    def parse_from(file_path: str, name: str) -> Problem:
        with open(file_path, "r") as file:
            lines = [line.replace('\n', '') for line in file]


        first_line = lines[0].split(" ")
        book_nb = int(first_line[0])
        lib_nb = int(first_line[1])
        dead_line = int(first_line[2])

        scores_book = lines[1].split(" ")

        books = []
        idx = 0
        for sc in scores_book:
            books.append(Book(idx, int(sc)))
            idx += 1

        libraries = []
        for lib_idx in range(lib_nb):
            lib_line = lines[2+lib_idx*2].split(" ")
            lib_book_nb = int(lib_line[0])
            signup = int(lib_line[1])
            lib_ship_capacity = int(lib_line[2])

            lib_book_line = lines[2+lib_idx*2 + 1].split(" ")

            lib_books = []
            for lb in lib_book_line:
                lib_books.append(books[int(lb)])
            libraries.append(Library(books=lib_books, sign_time=signup, books_per_day=lib_ship_capacity, id=lib_idx))

            lib_idx += 1



        return Problem(name=name, books=books, libraries=libraries, deadline=dead_line)
