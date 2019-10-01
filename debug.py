import json
from typing import List, Dict

from fitness import fitness


def peek_population(population: List[object]):
    population.sort(key=lambda individual_schedule: fitness(individual_schedule), reverse=True)
    kept_indices = int(len(population) * 0.2)
    best_individual = population[0]
    best_fitness_list: list = []
    for index in range(kept_indices):
        individual = population[index]
        best_fitness_list.append(fitness(individual))
    # best_fitness_str = ', '.join(best_fitness_list)
    # unique_individuals = len(list(set(population)))
    # distribution: list = Counter(population).values()
    population_dict = population_counter(population)
    print(f'Best individual [{fitness(best_individual)}]: \t{best_individual}')
    print(f'Unique: \t\t\t\t{len(population_dict)}')
    print(f'Best indices: \t\t\t{best_fitness_list}')
    print(f'Distribution: \t\t\t{sorted(population_dict.values(), reverse=True)}')
    print('\n')


def population_counter(population: List[object]):
    pop_dict: Dict[str, int] = {}
    for individual in population:
        individual_str = json.dumps(individual, sort_keys=True)
        pop_dict[individual_str] = pop_dict[individual_str] + 1 if individual_str in pop_dict.keys() else 1
    return pop_dict