from copy import deepcopy
from random import random, randint, randrange


def mutate_population(population, mutation_percentage, mutation_flavor_percentage):
    for index, individual in enumerate(population):
        mutation_factor = random()
        if mutation_factor < mutation_percentage:
            population[index] = mutate_individual(individual, mutation_flavor_percentage)


def swap_days(candidate):
    class_index = randrange(len(candidate))
    first_index = randrange(len(candidate[class_index]))
    second_index = first_index
    while candidate[class_index][first_index] == candidate[class_index][second_index]:
        second_index = randrange(len(candidate[class_index]))
    candidate[class_index][first_index], candidate[class_index][second_index] = \
        candidate[class_index][second_index], candidate[class_index][first_index]
    print(f'Swapped days {first_index} and {second_index} for class {class_index}')
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
    while candidate[class_index][first_day_index][first_index] == candidate[class_index][second_day_index][second_index]:
        second_index = randrange(len(second_day))
    candidate[class_index][first_day_index][first_index], candidate[class_index][second_day_index][second_index] = \
        candidate[class_index][second_day_index][second_index], candidate[class_index][first_day_index][first_index]
    print(f'Swapped subjects day {first_day_index} subject {first_index} '
          f'with day {second_day_index} subject {second_index} for class {class_index}')
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
    return randint()


def selector(population):
    new_population = []
    fitnesses = [fitness(candidate) for candidate in population]
    fitnesses = [fitness_score / sum(fitnesses) for fitness_score in fitnesses]
    fitnesses = [fitness_score + sum(fitnesses[0:current_index]) for current_index, fitness_score in enumerate(fitnesses)]
    for pop_index in range(len(population)):
        chosen_value = random()
        # TODO: Binary search in this bitch
        for fitness_index in range(len(fitnesses)):
            if fitnesses[fitness_index] > chosen_value:
                new_population.append(deepcopy(population[fitness_index]))
    return new_population


if __name__ == '__main__':
    candidate = \
        [                     # List of classes
            [                 # List of days
                [1, 8, 2],    # List of subjects
                [5, 1, 7],
                [1, 4]],
            [
                [5, 1, 7],
                [1, 8, 2],
                [7, 2]
            ]
        ]
    mutate_individual(candidate, 1)
    mutate_individual(candidate, 0)
    print(candidate)
    exit(0)
