import json
from typing import List, Dict

from fitness import fitness


def peek_population(population: List[object]):
    population.sort(key=lambda individual_schedule: fitness(individual_schedule), reverse=True)
    best_individual = population[0]
    # best_fitness_list: list = get_top_best_fitness_list(population, kept_indices)
    population_dict = population_counter(population)
    # print(f'Best individual [{fitness(best_individual)}]: \t{best_individual}')
    print(f'Unique: \t\t\t\t{len(population_dict)}')
    # print(f'Best indices: \t\t\t{best_fitness_list}')
    print(f'Distribution: \t\t\t{sorted(population_dict.values(), reverse=True)}')
    return best_individual, population_dict


def get_top_best_fitness_list(population, top_percent = 0.2) -> list:
    kept_indices = int(len(population) * top_percent)
    best_fitness_list = []
    for index in range(kept_indices):
        best_fitness_list.append(fitness(population[index]))
    return best_fitness_list


def population_counter(population: List[object]):
    pop_dict: Dict[str, int] = {}
    for individual in population:
        individual_str = json.dumps(individual, sort_keys=True)
        pop_dict[individual_str] = pop_dict[individual_str] + 1 if individual_str in pop_dict.keys() else 1
    return pop_dict
