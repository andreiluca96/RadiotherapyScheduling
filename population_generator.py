from itertools import islice
from random import shuffle, randint

from input.utils import get_input, print_schedule, print_schedule_teacher


def randomize_days_length(total_number_of_days, chunks):
    """
    Split the number of sessions in a week into roughly random chunks, but in random order
    Ex: 13 sessions in 5 days might return: [3,3,2,3,2] or [2,3,3,2,3] or any other permutation
    """
    result = []
    total_sum = 0
    division = total_number_of_days / chunks
    for i in range(chunks):
        i_division = round((i + 1) * division)
        i_division -= total_sum
        total_sum += i_division
        result.append(i_division)
    shuffle(result)
    return result


def random_chunks(li, size_list):
    """
    Return an iterator that outputs
    :param li:
    :param size_list:
    :return:
    """
    index = 0
    it = iter(li)
    while True:
        if index == len(size_list):
            break

        nxt = list(islice(it, size_list[index]))
        index += 1
        if nxt:
            yield nxt
        else:
            break


def generate_population(patient_number: int, pop_size=100):
    pop = []
    for individual in range(pop_size):
        ind = []
        allocated_patient_number = randint(1, patient_number)
        while len(pop) < allocated_patient_number:
            chosen_patient = randint(1, patient_number)
            if chosen_patient not in ind:
                ind.append(chosen_patient)
        pop.append(ind)
    return pop


if __name__ == '__main__':
    patient_number = 20
    input_data = get_input(patient_number)

    population = generate_population(patient_number=patient_number)

    selected_individual = population[0]
    print('done')
