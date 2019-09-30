import time
from copy import deepcopy
from random import random, randint, randrange

from input.utils import get_input, print_schedule
from population_generator import generate_population


def mutate_population(population, mutation_percentage, mutation_flavor_percentage):
    for index, individual in enumerate(population):
        mutation_factor = random()
        if mutation_factor < mutation_percentage:
            population[index] = mutate_individual(individual, mutation_flavor_percentage)


# This implementation allows for an individual to be crossed over multiple times
def crossover_population(population, crossover_percentage):
    for index, individual in enumerate(population):
        crossover_factor = random()
        if crossover_factor < crossover_percentage:
            first_index = randrange(len(population))
            second_index = randrange(len(population))
            while first_index == second_index:
                second_index = randrange(len(population))
            population[first_index], population[second_index] = \
                crossover(population[first_index], population[second_index])


def swap_days(candidate):
    class_index = randrange(len(candidate))
    first_index = randrange(len(candidate[class_index]))
    second_index = randrange(len(candidate[class_index]))
    while candidate[class_index][first_index] == candidate[class_index][second_index]:
        second_index = randrange(len(candidate[class_index]))
    candidate[class_index][first_index], candidate[class_index][second_index] = \
        candidate[class_index][second_index], candidate[class_index][first_index]
    # print(f'Swapped days {first_index} and {second_index} for class {class_index}')
    return candidate


def swap_subjects(candidate):
    class_index = randrange(len(candidate))
    first_day_index = randrange(len(candidate[class_index]))
    second_day_index = randrange(len(candidate[class_index]))
    while second_day_index == first_day_index:
        second_day_index = randrange(len(candidate[class_index]))
    first_day = candidate[class_index][first_day_index]
    first_index = randrange(len(first_day))
    second_day = candidate[class_index][second_day_index]
    second_index = randrange(len(second_day))
    it_number = 0
    while candidate[class_index][first_day_index][first_index] == candidate[class_index][second_day_index][second_index]:
        second_index = randrange(len(second_day))
        it_number += 1
        if it_number > 20:
            return swap_subjects(candidate)
    candidate[class_index][first_day_index][first_index], candidate[class_index][second_day_index][second_index] = \
        candidate[class_index][second_day_index][second_index], candidate[class_index][first_day_index][first_index]
    # print(f'Swapped subjects day {first_day_index} subject {first_index} '
    #       f'with day {second_day_index} subject {second_index} for class {class_index}')
    return candidate


def mutate_individual(candidate, mutation_flavor_percentage):
    if random() < mutation_flavor_percentage:
        candidate = swap_days(candidate)
    else:
        candidate = swap_subjects(candidate)
    return candidate


def crossover(candidate1, candidate2):
    class_index = randrange(len(candidate1))
    candidate1[class_index], candidate2[class_index] = candidate2[class_index], candidate1[class_index]
    return candidate1, candidate2


def fitness(candidate):
    fitness_score = 0
    for day_index in range(5):
        for hour_index in range(7):
            ids = []
            for class_group in candidate:
                try:
                    ids.append(class_group[day_index][hour_index])
                except:
                    pass
            if len(ids) == len(set(ids)):
                fitness_score += 1
    return fitness_score


def selector(population):
    new_population = []
    fitness_scores = [fitness(candidate) for candidate in population]
    print(f'Best fitness score is {max(fitness_scores)}')
    fitness_scores = [fitness_score / sum(fitness_scores) for fitness_score in fitness_scores]
    fitness_scores = [fitness_score + sum(fitness_scores[0:current_index])
                      for current_index, fitness_score in enumerate(fitness_scores)]
    for pop_index in range(len(population)):
        chosen_value = random()
        for fitness_index in range(len(fitness_scores)):
            if fitness_scores[fitness_index] > chosen_value:
                new_population.append(deepcopy(population[fitness_index]))
                break
    return new_population


def elitist_selector(population):
    population.sort(key=lambda individual: fitness(individual), reverse=True)
    kept_indices = int(len(population) * 0.2)
    new_population = [deepcopy(population[index % kept_indices]) for index in range(len(population))]
    return new_population


def genetic_algorithm(classes,
                      population_size=100,
                      iterations=1000,
                      mutation_percentage=0.15,
                      mutation_flavor_percentage=0.3,
                      crossover_percentage=0.15):
    population = generate_population(classes, population_size)
    best_fitness = 0
    it = 0
    # for iteration in range(iterations):
    while best_fitness < 35:
        it += 1
        if it % 100 == 0:
            print(f'Iteration {it}')
        # print(f'Iteration {iteration}')
        # population = selector(population)
        fitness_scores = [fitness(candidate) for candidate in population]
        # print(f'Best fitness score is {max(fitness_scores)}')
        population = elitist_selector(population)
        mutate_population(population, mutation_percentage, mutation_flavor_percentage)
        crossover_population(population, crossover_percentage)
        new_maximum = max([fitness(candidate) for candidate in population])
        if new_maximum > best_fitness:
            print(f'New maximum obtained ({new_maximum})')
            best_fitness = new_maximum
    # print(f'Best individual: {max(population, key=lambda candidate: fitness(candidate))} '
    #       f'(score: {max([fitness(candidate) for candidate in population])})')
    # with open('results.txt', 'a') as f:
    #     f.write(f'{max([fitness(candidate) for candidate in population])} {max(population, key=lambda candidate: fitness(candidate))}\n')
    return max(population, key=lambda candidate: fitness(candidate))


if __name__ == '__main__':
    # candidate = \
    #     [                     # List of classes
    #         [                 # List of days
    #             [1, 8, 2],    # List of subjects
    #             [5, 1, 7],
    #             [1, 4]],
    #         [
    #             [5, 1, 7],
    #             [1, 8, 2],
    #             [7, 2]
    #         ]
    #     ]
    # mutate_individual(candidate, 1)
    # mutate_individual(candidate, 0)
    # print(candidate)
    # selector(list(range(10)))
    # exit(0)
    input_data = get_input()
    all_classes = input_data["assignments"]
    selected_individual = genetic_algorithm(all_classes)
    # for class_index in range(len(selected_individual)):
    #     print_schedule(
    #         title=input_data["classes"][class_index],
    #         teachers=input_data["teachers"],
    #         schedule=selected_individual[class_index]
    #     )
