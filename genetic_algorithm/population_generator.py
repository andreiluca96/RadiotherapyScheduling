from itertools import islice
import random

from input.utils import get_input


def generate_population(problem_input: {}, pop_size=100):
    pop = []
    for individual in range(pop_size):
        ind = list(range(1, problem_input['patients'] + 1))

        random.shuffle(ind)

        pop.append(ind)
    return pop


if __name__ == '__main__':
    input_data = get_input()
    print(input_data)
    population = generate_population(input_data, pop_size=5)

    print(population)
