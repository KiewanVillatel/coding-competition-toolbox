from __future__ import annotations

import abc
import pickle
from hashcode.model.problem import Problem


class Solution:

    def __init__(self, problem: Problem):
        self._problem = problem

    @staticmethod
    @abc.abstractmethod
    def generate_solution(problem: Problem) -> Solution:
        print("Computing solution")
        return Solution(problem)

    def build_out_file(self, path: str):
        with open(path, "w") as file:
            file.write("Dummy solution")

    def serialize(self, path: str):
        with open(path, "wb") as file:
            pickle.dump(self, file)

    def compute_score(self) -> float:
        return 0

    @staticmethod
    def crossover(sol1: Solution, sol2: Solution) -> Solution:
        return sol1

    @staticmethod
    def mutation(sol: Solution) -> Solution:
        return sol

    @staticmethod
    def evaluate(sol: Solution) -> float:
        return sol.compute_score()
