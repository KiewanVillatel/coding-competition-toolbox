from __future__ import annotations

import abc
import pickle
from hashcode.model.problem import Problem


class Solution:

    def __init__(self, problem: Problem):
        self._problem = problem
        self.libraries_sign_up = []

    @staticmethod
    @abc.abstractmethod
    def generate_solution(problem: Problem) -> Solution:
        print("Computing solution")
        return Solution(problem)

    def build_out_file(self, path: str):
        with open(path, "w") as file:
            lines = [str(len(self.libraries_sign_up))]

            for (library, books) in self.libraries_sign_up:
                lines.append("{} {}".format(library.id, len(books)))
                lines.append(" ".join(books))
            file.writelines(lines)

    def serialize(self, path: str):
        with open(path, "wb") as file:
            pickle.dump(self, file)

    def compute_score(self) -> float:
        score = 0
        for (library, books) in self.libraries_sign_up:
            score += sum([b.score for b in books])
        return score

    @staticmethod
    def crossover(sol1: Solution, sol2: Solution) -> Solution:
        return sol1

    @staticmethod
    def mutation(sol: Solution) -> Solution:
        return sol

    @staticmethod
    def evaluate(sol: Solution) -> float:
        return sol.compute_score()
