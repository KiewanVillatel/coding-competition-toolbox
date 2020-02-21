import calendar
import pickle
import time
from os import listdir, mkdir
from os.path import isfile, join, isdir

import click

from algos.genetic_algorithm import GeneticAlgorithm
from hashcode.model.dummy_solution import DummySolution
from hashcode.model.greedy_solution import GreedySolution
from hashcode.model.problem import Problem
from hashcode.model.solution import Solution


@click.group()
def main():
    pass


def serialize_solution(solution: Solution, sol_folder: str, test_case_name: str):
    sol_file_path = join(sol_folder, test_case_name) + ".sol"
    solution.build_out_file(sol_file_path)

    pickle_file_path = join(sol_folder, test_case_name) + ".pickle"
    solution.serialize(pickle_file_path)


@main.command()
@click.option("-i", "--input_path", help="Path to folder containing test cases", default="test_cases")
@click.option("-o", "--output_path", help="Path to folder to store solutions", default="out")
def compute_solutions(input_path: str, output_path: str):
    # Build directory for solutions
    sol_folder = join(output_path, "sol_" + str(calendar.timegm(time.gmtime())))
    mkdir(sol_folder)

    # Run test cases
    test_cases = [f for f in listdir(input_path) if isfile(join(input_path, f)) and f.endswith(".txt")]
    test_cases.sort()
    # test_cases = test_cases[0:1]
    total_score = 0
    for test_case in test_cases:
        test_case_name = test_case.split(".")[0]
        print("Processing test case {}".format(test_case))
        problem = Problem.parse_from(file_path=join(input_path, test_case),
                                     name=test_case_name)
        solution = GreedySolution.generate_solution(problem=problem)

        serialize_solution(solution=solution,
                           sol_folder=sol_folder,
                           test_case_name=test_case_name)

        solution_score = solution.compute_score()
        print("Score for test case {} : {} \n".format(test_case, solution_score))
        total_score += solution_score

    print("Total score : {}".format(total_score))


@main.command()
@click.option("-i", "--input_path", help="Path to folder containing test cases", default="out")
def genetic_algorithm(input_path: str):
    # Retrieve all solutions files
    solutions_paths = {}
    sol_folders = [join(input_path, f) for f in listdir(input_path) if isdir(join(input_path, f))]
    for sol_folder in sol_folders:
        test_cases = [f for f in listdir(sol_folder) if isfile(join(sol_folder, f)) and f.endswith(".pickle")]

        for test_case in test_cases:
            if test_case not in solutions_paths:
                solutions_paths[test_case] = []

            solutions_paths[test_case].append(join(sol_folder, test_case))

    # Create directory to genetic algorithm solutions
    sol_folder = "{}/sol_{}".format(input_path, calendar.timegm(time.gmtime()))
    mkdir(sol_folder)

    for test_case in solutions_paths:
        test_case_name = test_case.split(".")[0]
        initial_pop = []
        for solution_path in solutions_paths[test_case]:
            with open(solution_path, "rb") as file:
                solution = pickle.load(file)
                initial_pop.append(solution)

        # Run genetic algorithm
        gen_algo = GeneticAlgorithm(eval_fn=Solution.evaluate,
                                    crossover_fn=Solution.crossover,
                                    mutation_fn=Solution.mutation)

        gen_algo.run(initial_pop, iterations=100)

        # Serialize best solution
        best_sol = max(initial_pop, key=lambda s: s.compute_score())

        serialize_solution(solution=best_sol,
                           sol_folder=sol_folder,
                           test_case_name=test_case_name)


if __name__ == "__main__":
    main()
