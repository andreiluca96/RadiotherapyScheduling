from itertools import islice
import random

from genetic_algorithm.ga_iterator import GA
from input.utils import get_input


limits = \
    {
        'population': (25, 200),
        'mutation': (0.01, 0.7),
        'crossover': (0.01, 0.7),
        'iterations': (50, 120)
    }


def generate_genetic_population(pop_size=100):
    pop = []
    for individual in range(pop_size):
        ind = GA(population_size=random.randrange(*limits['population']),
                 iterations=random.randrange(*limits['iterations']),
                 mutation_percentage=random.uniform(*limits['mutation']),
                 crossover_percentage=random.uniform(*limits['crossover']))
        pop.append(ind)
    return pop


if __name__ == '__main__':
    input_data = get_input()
    print(input_data)
    population = generate_genetic_population(pop_size=5)

    print(population)
