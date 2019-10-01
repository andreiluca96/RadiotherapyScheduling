import time

from debug import peek_population
from fitness import fitness
from ga_operators import crossover_population, mutate_population
from input.utils import get_input, print_schedule
from population_generator import generate_population
from selectors import elitist_selector


def genetic_algorithm(classes,
                      population_size=100,
                      iterations=1000,
                      mutation_percentage=0.5,
                      mutation_flavor_percentage=0.3,
                      crossover_percentage=0.5):
    population = generate_population(classes, population_size)
    best_fitness = 0
    it = 0
    while best_fitness < 35:
        it += 1
        if iterations is not None and it >= iterations:
            print('Maximum iterations reached')
            break

        if it % 100 == 0:
            print(f'Iteration {it}')
        # print(f'Iteration {iteration}')
        # population = selector(population)
        # fitness_scores = [fitness(candidate) for candidate in population]
        # print(f'Best fitness score is {max(fitness_scores)}')
        population = elitist_selector(population)
        mutate_population(population, mutation_percentage, mutation_flavor_percentage)
        crossover_population(population, crossover_percentage)
        # best_individual = max(population, key=lambda candidate: fitness(candidate))
        # print(f'Best individual: {best_individual} (score: {fitness(best_individual)})')
        print(it)
        peek_population(population)
        new_maximum = max([fitness(candidate) for candidate in population])
        if new_maximum > best_fitness:
            print(f'New maximum obtained ({new_maximum})')
            best_fitness = new_maximum
    with open('results.txt', 'a') as f:
        f.write(f'{max([fitness(candidate) for candidate in population])} {max(population, key=lambda candidate: fitness(candidate))}\n')
    return max(population, key=lambda candidate: fitness(candidate))


if __name__ == '__main__':
    for it in range(96):
        start_time = time.time()
        input_data = get_input()
        all_classes = input_data["assignments"]
        selected_individual = genetic_algorithm(all_classes)
        print(f'Time: {time.time() - start_time}')
    # for class_index in range(len(selected_individual)):
    #     print_schedule(
    #         title=input_data["classes"][class_index],
    #         teachers=input_data["teachers"],
    #         schedule=selected_individual[class_index]
    #     )
