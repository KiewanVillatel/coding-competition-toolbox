from __future__ import annotations

import abc
import pickle

from hashcode.model.book import Book
from hashcode.model.library import Library
from hashcode.model.problem import Problem


class Solution:

    def __init__(self, problem: Problem):
        self._problem = problem
        self.scans = []

    @staticmethod
    @abc.abstractmethod
    def generate_solution(problem: Problem) -> Solution:
        print("Computing solution")
        return Solution(problem)

    def build_out_file(self, path: str):
        with open(path, "w") as file:
            lines = [str(len(self.scans))+ "\n"]

            for scan in self.scans:
                lines.append("{} {} \n".format(scan.library.id, len(scan.books)))
                lines.append(" ".join([str(book.id) for book in scan.books]) + "\n")
            file.writelines(lines)

    def serialize(self, path: str):
        with open(path, "wb") as file:
            pickle.dump(self, file)

    def compute_score(self) -> float:
        score = 0
        for scan in self.scans:
            score += sum([b.score for b in scan.books])
        return score

    def scan_book(self, library: Library, book: Book):
        for scan in self.scans:
            if scan.library == library:
                scan.books.append(book)
                return

    @staticmethod
    def crossover(sol1: Solution, sol2: Solution) -> Solution:
        return sol1

    @staticmethod
    def mutation(sol: Solution) -> Solution:
        return sol

    @staticmethod
    def evaluate(sol: Solution) -> float:
        return sol.compute_score()
