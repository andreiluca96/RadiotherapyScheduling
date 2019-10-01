import json
import time

from debug import peek_population
from fitness import fitness
from ga_operators import crossover_population, mutate_population
from input.utils import get_input, print_schedule
from population_generator import generate_population
from selectors import elitist_selector


class GA(object):
    def __init__(self, population_size=100,
                 iterations=None,
                 mutation_percentage=0.5,
                 mutation_flavor_percentage=0.3,
                 crossover_percentage=0.5) -> None:
        self.population_size = population_size
        self.iterations = iterations
        self.mutation_percentage = mutation_percentage
        self.mutation_flavor_percentage = mutation_flavor_percentage
        self.crossover_percentage = crossover_percentage

    def genetic_algorithm(self, classes):
        population = generate_population(classes, self.population_size)
        best_fitness = 0
        best_individual = ''
        it = 0
        while best_fitness < 35:
            print('\n')
            it += 1
            if self.iterations is not None and it >= self.iterations:
                print(f'Maximum iterations reached. Best fitness {best_fitness}')
                break

            if it % 100 == 0:
                print(f'Iteration {it}')
            # print(f'Iteration {iteration}')
            # population = selector(population)
            # fitness_scores = [fitness(candidate) for candidate in population]
            # print(f'Best fitness score is {max(fitness_scores)}')
            population = elitist_selector(population)
            mutate_population(population, self.mutation_percentage, self.mutation_flavor_percentage)
            crossover_population(population, self.crossover_percentage)
            # best_individual = max(population, key=lambda candidate: fitness(candidate))
            # print(f'Best individual: {best_individual} (score: {fitness(best_individual)})')
            # print(it)
            best_current_individual, _ = peek_population(population)
            best_individual_str = json.dumps(best_current_individual, sort_keys=True)
            if best_individual_str != best_individual:
                best_individual = best_individual_str
                print(f'Best individual [{fitness(best_individual)}]: \t{best_individual}')
            new_maximum = max([fitness(candidate) for candidate in population])
            if new_maximum > best_fitness:
                print(f'New maximum obtained ({new_maximum}) in iteration {it}')
                best_fitness = new_maximum

        with open('results.txt', 'a') as f:
            f.write(
                f'{max([fitness(candidate) for candidate in population])} {max(population, key=lambda candidate: fitness(candidate))}\n')

        return max(population, key=lambda candidate: fitness(candidate))


if __name__ == '__main__':
    ga = GA()
    # input_data = {}
    # selected_individual = []
    # for it in range(96):
    start_time = time.time()
    input_data = get_input()
    all_classes = input_data["assignments"]
    selected_individual = ga.genetic_algorithm(all_classes)
    print(f'Time: {time.time() - start_time}')
    for class_index in range(len(selected_individual)):
        print_schedule(
            title=input_data["classes"][class_index],
            teachers=input_data["teachers"],
            schedule=selected_individual[class_index]
        )
