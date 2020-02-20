from hashcode.model.Scan import Scan
from hashcode.model.problem import Problem
from hashcode.model.solution import Solution


class DummySolution(Solution):

    def __init__(self, problem: Problem):
        super().__init__(problem)

    @staticmethod
    def generate_solution(problem: Problem) -> Solution:
        sol = DummySolution(problem)
        sol.scans.append(Scan(problem.libraries[0], [list(problem.libraries[0].books)[0]]))
        return sol
