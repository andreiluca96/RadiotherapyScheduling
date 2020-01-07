from genetic_algorithm.ga_iterator import GA


def fitness(candidate: GA, input_data: {}):
    return candidate.genetic_algorithm(input_data)[1]
