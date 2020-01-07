from copy import deepcopy
from random import randrange, random

from genetic_algorithm.ga_iterator import GA
from metagenetic_algorithm.metapopulation_generator import limits


def crossover(parent1: GA, parent2: GA):
    # In alphabetical order: crossover, iterations, mutation, population
    cutoff_point = randrange(0, 4)
    parent1.crossover_percentage, parent2.crossover_percentage = parent2.crossover_percentage, parent1.crossover_percentage
    if cutoff_point > 0:
        parent1.iterations, parent2.iterations = parent2.iterations, parent1.iterations
        if cutoff_point > 1:
            parent1.mutation_percentage, parent2.mutation_percentage = parent2.mutation_percentage, parent1.mutation_percentage
            if cutoff_point > 2:
                parent1.population_size, parent2.population_size = parent2.population_size, parent1.population_size
    return deepcopy(parent1), deepcopy(parent2)


def mutate(individual: GA, mutation_rate):
    # population
    if random() < mutation_rate:
        individual.population_size = randrange(*limits['population'])
    # mutation
    if random() < mutation_rate:
        individual.mutation_percentage = randrange(*limits['mutation'])
    # crossover
    if random() < mutation_rate:
        individual.crossover_percentage = randrange(*limits['crossover'])
    # iterations
    if random() < mutation_rate:
        individual.iterations = randrange(*limits['iterations'])
    return individual


def crossover_population(population, crossover_percentage):
    for index, individual in enumerate(population):
        crossover_factor = random()
        if crossover_factor < crossover_percentage:
            first_index = index

            second_index = randrange(len(population))
            while first_index == second_index:
                second_index = randrange(len(population))

            population[first_index], population[second_index] = crossover(population[first_index], population[second_index])


def mutate_population(population, mutation_percentage):
    for index, individual in enumerate(population):
        population[index] = mutate(individual, mutation_percentage)
