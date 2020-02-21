from hashcode.model.Scan import Scan
from hashcode.model.problem import Problem
from hashcode.model.solution import Solution


class GreedySolution(Solution):

    def __init__(self, problem: Problem):
        super().__init__(problem)

    @staticmethod
    def generate_solution(problem: Problem) -> Solution:
        sol = GreedySolution(problem)

        iter = 0
        timestep = 0
        while timestep < problem.deadline:
            if iter % 1000 == 0:
                print("Progress {}%".format((timestep * 100) // problem.deadline))
            if not len(sol._problem.libraries):
                break
            library = sol.get_library()
            sol._problem.libraries.remove(library)
            timestep += library.sign_time
            sol.scan_books(library, timestep)
            iter += 1

        return sol

    def get_library(self):

        libraries = sorted(self._problem.libraries, key=lambda l: -l.get_score())

        best_lib = libraries.pop(0)

        return best_lib

    def get_books_to_scan(self, library, nb_books):
        library.books.sort(key=lambda b: -b.score)

        return library.books[:nb_books]

    def scan_books(self, library, current_timestep):
        nb_book_to_scan = (self._problem.deadline - current_timestep) * library.books_per_day

        books_to_scan = self.get_books_to_scan(library, nb_book_to_scan)

        if len(books_to_scan):
            self.scans.append(Scan(library, books_to_scan))

        for book in books_to_scan:
            for library in book.libraries:
                library.remove_book(book)
