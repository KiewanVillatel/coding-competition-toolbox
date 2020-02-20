from __future__ import annotations
from hashcode.model.book import Book
from hashcode.model.library import Library
from typing import List


class Problem:

    def __init__(self, name: str, books: List[Book], libraries: List[Library]):
        self.name = name
        self.books = books
        self.libraries = libraries

    @staticmethod
    def parse_from(file_path: str, name: str) -> Problem:
        with open(file_path, "r") as file:
            for line in file:
                print("Parsing line: {}".format(line))
        return Problem(name=name)
