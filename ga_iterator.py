import json
import time

from debug import peek_population
from fitness import fitness
from ga_operators import crossover_population, mutate_population
from input.utils import get_input, print_schedule
from population_generator import generate_population
from selectors import elitist_selector
import matplotlib.pyplot as plt
import numpy as np


class GA(object):
    def __init__(self,
                 population_size=100,
                 iterations=100,
                 mutation_percentage=0.5,
                 mutation_flavor_percentage=0.3,
                 crossover_percentage=0.5) -> None:
        self.population_size = population_size
        self.iterations = iterations
        self.mutation_percentage = mutation_percentage
        self.mutation_flavor_percentage = mutation_flavor_percentage
        self.crossover_percentage = crossover_percentage
        self.max_fitness = 35

    def genetic_algorithm(self, patient_number):
        population = generate_population(patient_number, self.population_size)
        data = {
            'max_fitness': [],
            'uniqueness': []
        }
        best_fitness = 0
        best_individual = ''
        it = 0
        # while best_fitness < self.max_fitness:
        while it < self.iterations:
            print('\n')
            it += 1

            if it % 100 == 0:
                print(f'Iteration {it}')
            # population = selector(population)
            population = elitist_selector(population)
            mutate_population(population, self.mutation_percentage, self.mutation_flavor_percentage)
            crossover_population(population, self.crossover_percentage)
            # best_individual = max(population, key=lambda candidate: fitness(candidate))

            new_maximum = max([fitness(candidate) for candidate in population])
            data['max_fitness'].append(new_maximum / self.max_fitness)
            if new_maximum > best_fitness:
                print(f'New maximum obtained ({new_maximum}) in iteration {it}')
                best_fitness = new_maximum

            best_current_individual, population_dict = peek_population(population)
            best_individual_str = json.dumps(best_current_individual, sort_keys=True)
            data['uniqueness'].append(len(population_dict)/100)
            if best_individual_str != best_individual:
                best_individual = best_individual_str
                # print(f'Best individual [{fitness(best_individual)}]: \t{best_individual}')

            if it % 100 == 0:
                plt.plot(np.arange(0, it), data['max_fitness'], c='m')
                plt.plot(np.arange(0, it), data['uniqueness'], c='r')
                plt.show()
        print(f'Maximum iterations reached. Best fitness {best_fitness}')

        with open('results.txt', 'a') as f:
            f.write(
                f'{max([fitness(candidate) for candidate in population])} {max(population, key=lambda candidate: fitness(candidate))}\n')

        return max(population, key=lambda candidate: fitness(candidate))


if __name__ == '__main__':
    start_time = time.time()
    input_data = get_input()
    all_classes = input_data["assignments"]
    selected_individual = GA().genetic_algorithm(all_classes)
    print(f'Time: {time.time() - start_time}')
    for class_index in range(len(selected_individual)):
        print_schedule(
            title=input_data["classes"][class_index],
            teachers=input_data["teachers"],
            schedule=selected_individual[class_index]
        )
