import time

from input.fitness import fitness
from genetic_algorithm.ga_operators import crossover_population, mutate_population
from input.utils import get_input
from genetic_algorithm.population_generator import generate_population
from genetic_algorithm.ga_selectors import elitist_selector
import matplotlib.pyplot as plt
import numpy as np


class GA(object):
    def __init__(self,
                 population_size=25,
                 iterations=500,
                 mutation_percentage=0.01,
                 crossover_percentage=0.25) -> None:
        self.population_size = population_size
        self.iterations = iterations
        self.mutation_percentage = mutation_percentage
        self.crossover_percentage = crossover_percentage

    def genetic_algorithm(self, problem_input=None):
        if problem_input is None:
            problem_input = get_input()

        population = generate_population(problem_input, self.population_size)

        data = {
            'max_fitness': []
        }
        best_fitness = 0
        best_individual = ''
        it = 0
        # while best_fitness < self.max_fitness:
        while it < self.iterations:
            # print('\n')
            it += 1

            if it % 100 == 0:
                print(f'Iteration {it}')
            # population = selector(population, input_data)
            population = elitist_selector(population, input_data=input_data)
            mutate_population(population, self.mutation_percentage)
            crossover_population(population, self.crossover_percentage)
            # best_individual = max(population, key=lambda candidate: fitness(candidate))

            new_maximum = max([fitness(candidate, input_data) for candidate in population])
            data['max_fitness'].append(new_maximum)
            if new_maximum > best_fitness:
                print(f'New maximum obtained ({new_maximum}) in iteration {it}')
                best_fitness = new_maximum

            # best_current_individual, population_dict = peek_population(population)
            # best_individual_str = json.dumps(best_current_individual, sort_keys=True)
            # data['uniqueness'].append(len(population_dict)/100)
            # if best_individual_str != best_individual:
            #     best_individual = best_individual_str
                # print(f'Best individual [{fitness(best_individual)}]: \t{best_individual}')

            if it % 25 == 0:
                plt.plot(np.arange(0, it), data['max_fitness'], c='m')
                # plt.plot(np.arange(0, it), data['uniqueness'], c='r')
        print(f'Maximum iterations reached. Best fitness {best_fitness}')

        with open('results.txt', 'a') as f:
            f.write(
                f'{max([fitness(candidate, input_data) for candidate in population])} {max(population, key=lambda candidate: fitness(candidate, input_data))}\n')

        return max(population, key=lambda candidate: fitness(candidate, input_data))


if __name__ == '__main__':
    start_time = time.time()
    input_data = get_input(patients=25)
    selected_individual = GA().genetic_algorithm(input_data)
    print(f'Time: {time.time() - start_time}')

    start_time = time.time()
    input_data = get_input(patients=50)
    selected_individual = GA().genetic_algorithm(input_data)
    print(f'Time: {time.time() - start_time}')

    start_time = time.time()
    input_data = get_input(patients=100)
    selected_individual = GA().genetic_algorithm(input_data)
    print(f'Time: {time.time() - start_time}')

    start_time = time.time()
    input_data = get_input(patients=150)
    selected_individual = GA().genetic_algorithm(input_data)
    print(f'Time: {time.time() - start_time}')


    plt.show()

    # for class_index in range(len(selected_individual)):
    #     print_schedule(
    #         title=input_data["classes"][class_index],
    #         teachers=input_data["teachers"],
    #         schedule=selected_individual[class_index]
    #     )
