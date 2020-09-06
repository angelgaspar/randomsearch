import random
import numpy as np


def optimize(function, dimensions, lower_boundary, upper_boundary, max_iter, maximize=False):
    best_solution = np.array([float()] * dimensions)

    for i in range(dimensions):
        best_solution[i] = random.uniform(lower_boundary[i], upper_boundary[i])

    for _ in range(max_iter):

        solution1 = function(best_solution)

        new_solution = [lower_boundary[d] + random.random() * (upper_boundary[d] - lower_boundary[d]) for d in
                        range(dimensions)]

        if np.greater_equal(new_solution, lower_boundary).all() and np.less_equal(new_solution, upper_boundary).all():
            solution2 = function(new_solution)
        elif maximize:
            solution2 = -100000.0
        else:
            solution2 = 100000.0

        if solution2 > solution1 and maximize:
            best_solution = new_solution
        elif solution2 < solution1 and not maximize:
            best_solution = new_solution

    best_fitness = function(best_solution)

    return best_fitness, best_solution
