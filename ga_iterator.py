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
    while second_index == first_index:
        second_index = randrange(len(candidate[class_index]))
    candidate[class_index][first_index], candidate[class_index][second_index] = \
        candidate[class_index][second_index], candidate[class_index][first_index]
    return candidate


def swap_subjects(candidate):
    class_index = randrange(len(candidate))
    day_index = randrange(len(candidate[class_index]))
    day = candidate[class_index][day_index]
    first_index = randrange(len(day))
    second_index = first_index
    while second_index == first_index:
        second_index = randrange(len(day))
    day[first_index], day[second_index] = day[second_index], day[first_index]
    return candidate


def mutate_individual(candidate, mutation_flavor_percentage):
    if random() < mutation_flavor_percentage:
        candidate = swap_days(candidate)
    else:
        candidate = swap_subjects(candidate)
    return candidate


if __name__ == '__main__':
    candidate = [[[1, 8, 2], [5, 1, 7], [1, 4]], [[5, 1, 7], [1, 8, 2], [7, 2]]]
    mutate_individual(candidate, 1)
    mutate_individual(candidate, 0)
    exit(0)
