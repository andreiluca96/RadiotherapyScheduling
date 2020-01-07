import time

from genetic_algorithm.population_generator import generate_population
from input.utils import get_input
import matplotlib.pyplot as plt
import numpy as np

from metagenetic_algorithm.metaga_operators import mutate_population, crossover_population
from metagenetic_algorithm.metaga_selectors import elitist_selector
from metagenetic_algorithm.metapopulation_generator import generate_genetic_population


class MetaGA(object):
    def __init__(self,
                 patient_population_size=25,
                 population_size=25,
                 iterations=500,
                 mutation_percentage=0.01,
                 crossover_percentage=0.25) -> None:
        self.patient_population_size = patient_population_size
        self.population_size = population_size
        self.iterations = iterations
        self.mutation_percentage = mutation_percentage
        self.crossover_percentage = crossover_percentage

    def genetic_algorithm(self, problem_input=None):
        # Generate patient input
        if problem_input is None:
            problem_input = get_input()

        # Generate patient population
        population = generate_population(problem_input, self.patient_population_size)
        scores = []

        data = {
            'max_fitness': []
        }

        # Generate genetic population
        genetic_population = generate_genetic_population(self.population_size)

        best_fitness = 0
        best_individual = ''
        it = 0
        # while best_fitness < self.max_fitness:
        while it < self.iterations:
            # print('\n')
            it += 1
            print(f'--- METAITERATION {it} ---')

            # population = selector(population, input_data)
            population, scores = elitist_selector(genetic_population, input_data=problem_input)
            new_maximum = max(scores)
            data['max_fitness'].append(new_maximum)
            if new_maximum > best_fitness:
                print(f'New maximum obtained ({new_maximum}) in iteration {it}')
                best_fitness = new_maximum

            if it < self.iterations:
                mutate_population(population, self.mutation_percentage)
                crossover_population(population, self.crossover_percentage)

            if it % 25 == 0:
                plt.plot(np.arange(0, it), data['max_fitness'], c='m')
                # plt.plot(np.arange(0, it), data['uniqueness'], c='r')
        print(f'Maximum iterations reached. Best fitness {best_fitness}')

        return [pair[1] for pair in sorted(list(zip(scores, population)), reverse=True)][0]


if __name__ == '__main__':
    start_time = time.time()
    input_data = get_input(patients=50, days=10, slots=6, max_treatment_days=6)
    selected_individual = MetaGA(population_size=10).genetic_algorithm(input_data)
    print(f'Time: {time.time() - start_time}')


    plt.show()

    # for class_index in range(len(selected_individual)):
    #     print_schedule(
    #         title=input_data["classes"][class_index],
    #         teachers=input_data["teachers"],
    #         schedule=selected_individual[class_index]
    #     )
