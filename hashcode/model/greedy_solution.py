from hashcode.model.Scan import Scan
from hashcode.model.book import Book
from hashcode.model.library import Library
from hashcode.model.problem import Problem
from hashcode.model.solution import Solution


class GreedySolution(Solution):

    def __init__(self, problem: Problem):
        super().__init__(problem)

    @staticmethod
    def generate_solution(problem: Problem) -> Solution:
        sol = GreedySolution(problem)

        book_scanned = [False for _ in range(len(problem.books))]

        libraries_to_sign = [l for l in problem.libraries]
        signed_libraries = []
        current_signed_library = problem.libraries[0]
        libraries_to_sign.remove(current_signed_library)
        remaining_time_to_sign = current_signed_library.sign_time

        for timestep in range(problem.deadline):
            print("Progress {}".format(float(timestep/problem.deadline)))
            if remaining_time_to_sign == 0:
                signed_libraries.append(current_signed_library)
                sol.scans.append(Scan(current_signed_library, []))
                if len(libraries_to_sign):
                    current_signed_library = libraries_to_sign.pop()
                    remaining_time_to_sign = current_signed_library.sign_time

            remaining_time_to_sign -= 1

            for library in signed_libraries:
                nb_book_scaned = 0
                for book in library.books:
                    if nb_book_scaned == library.books_per_day:
                        break

                    if not book_scanned[book.id]:
                        nb_book_scaned += 1
                        book_scanned[book.id] = True
                        sol.scan_book(library, book)

        return sol
