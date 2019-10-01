from random import randrange, random


def crossover(candidate1, candidate2):
    class_index = randrange(len(candidate1))
    candidate1[class_index], candidate2[class_index] = candidate2[class_index], candidate1[class_index]
    return candidate1, candidate2


def mutate_individual(candidate, mutation_flavor_percentage):
    if random() < mutation_flavor_percentage:
        candidate = swap_days(candidate)
    else:
        candidate = swap_subjects(candidate)
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


def mutate_population(population, mutation_percentage, mutation_flavor_percentage):
    for index, individual in enumerate(population):
        mutation_factor = random()
        if mutation_factor < mutation_percentage:
            population[index] = mutate_individual(individual, mutation_flavor_percentage)