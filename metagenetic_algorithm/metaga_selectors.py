from copy import deepcopy
from random import random

from metagenetic_algorithm.fitness import fitness


def elitist_selector(population, input_data):
    scores = [fitness(individual, input_data=input_data) for individual in population]
    population = [pair[1] for pair in sorted(list(zip(scores, population)), reverse=True)]
    kept_indices = int(len(population) * 0.2)
    if kept_indices == 0:
        kept_indices = 1
    new_population = [deepcopy(population[index % kept_indices]) for index in range(len(population))]
    new_scores = [scores[index % kept_indices] for index in range(len(population))]
    return new_population, new_scores


def selector(population, input_data):
    new_population = []
    fitness_scores = [fitness(candidate, input_data) for candidate in population]
    # print(f'Best fitness score is {max(fitness_scores)}')
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