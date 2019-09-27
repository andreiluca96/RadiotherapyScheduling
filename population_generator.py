from itertools import islice
from random import randint, shuffle


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


def generate_population(classes: list, pop_size=100, days_count=5):
    all_class_variants = []
    for class_group in classes:
        week_size = randomize_days_length(len(class_group), days_count)
        class_variants = []

        for individual in range(pop_size):
            class_variants.append(generate_class_schedule(class_group, week_size))
        all_class_variants.append(class_variants)

    population = []
    for option_index in range(pop_size):
        population.append([all_class_variants[class_index][option_index] for class_index in range(len(classes))])
    return population


def generate_class_schedule(subjects, subjects_per_day):
    """
    Generate schedule for a single class
    :param days_count:
    :param subjects:
    :param subjects_per_day:
    :return:
    """
    shuff_subjects = subjects.copy()
    shuffle(shuff_subjects)
    chunks = list(random_chunks(shuff_subjects, size_list=subjects_per_day))
    shuff_days = chunks.copy()
    shuffle(shuff_days)
    return shuff_days


if __name__ == '__main__':
    class_1 = [
        0, 0, 0, 0, 0,
        1, 1, 1, 1, 1,
        2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7
    ]

    class_2 = [
        9, 9, 9, 9, 9,
        10, 10, 10, 10, 10,
        2, 2, 3, 3, 4, 4, 5, 5, 8, 8, 7
    ]

    all_classes = [class_1, class_2]

    population = generate_population(
        classes=all_classes,
        pop_size=10
    )
    print('done')
