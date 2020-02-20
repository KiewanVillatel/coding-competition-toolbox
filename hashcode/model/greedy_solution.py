from hashcode.model.Scan import Scan
from hashcode.model.book import Book
from hashcode.model.library import Library
from hashcode.model.problem import Problem
from hashcode.model.solution import Solution


class GreedySolution(Solution):

    def __init__(self, problem: Problem):
        super().__init__(problem)


    def get_next_library(self):
        returned_lib = None
        max_lib_score = 0
        for lib in self.libraries_to_sign:
            score = lib.get_score()
            if score >= max_lib_score:
                max_lib_score = score
                returned_lib = lib
        return returned_lib


    def remove_book_in_librairies(self, book: Book):
        for lib in self.signed_libraries:
            lib.remove_book(book)



    @staticmethod
    def generate_solution(problem: Problem) -> Solution:
        sol = GreedySolution(problem)

        book_scanned = [False for _ in range(len(problem.books))]

        sol.libraries_to_sign = [l for l in problem.libraries]
        sol.signed_libraries = []
        current_signed_library = sol.get_next_library()
        sol.libraries_to_sign.remove(current_signed_library)
        remaining_time_to_sign = current_signed_library.sign_time

        for timestep in range(problem.deadline):
            if timestep % ((max(problem.deadline//1000, 1)) * 10) == 0:
                print("Progress {}".format(float(timestep/problem.deadline)))
            if remaining_time_to_sign == 0:
                sol.signed_libraries.append(current_signed_library)
                sol.scans.append(Scan(current_signed_library, []))
                if len(sol.libraries_to_sign):
                    current_signed_library = sol.get_next_library()
                    remaining_time_to_sign = current_signed_library.sign_time

            remaining_time_to_sign -= 1

            for library in sol.signed_libraries:
                nb_book_scaned = 0
                while len(library.books):
                    book = library.books.pop()
                    if nb_book_scaned == library.books_per_day:
                        break

                    if not book_scanned[book.id]:
                        nb_book_scaned += 1
                        book_scanned[book.id] = True
                        sol.scan_book(library, book)
                        sol.remove_book_in_librairies(book)

        return sol
