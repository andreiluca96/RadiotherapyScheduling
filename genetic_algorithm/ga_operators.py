from random import randrange, random


def crossover(parent1, parent2):
    child = []
    childP1 = []
    childP2 = []

    geneA = int(random() * len(parent1))
    geneB = int(random() * len(parent1))

    startGene = min(geneA, geneB)
    endGene = max(geneA, geneB)

    for i in range(startGene, endGene):
        childP1.append(parent1[i])

    childP2 = [item for item in parent2 if item not in childP1]

    child = childP1 + childP2
    return child


def mutate(individual, mutation_rate):
    for swapped in range(len(individual)):
        if random() < mutation_rate:
            swapWith = int(random() * len(individual))

            gene1 = individual[swapped]
            gene2 = individual[swapWith]

            individual[swapped] = gene2
            individual[swapWith] = gene1
    return individual


def crossover_population(population, crossover_percentage):
    for index, individual in enumerate(population):
        crossover_factor = random()
        if crossover_factor < crossover_percentage:
            first_index = index

            second_index = randrange(len(population))
            while first_index == second_index:
                second_index = randrange(len(population))

            population[first_index] = crossover(population[first_index], population[second_index])
            population[second_index] = crossover(population[second_index], population[first_index])


def mutate_population(population, mutation_percentage):
    for index, individual in enumerate(population):
        population[index] = mutate(individual, mutation_percentage)