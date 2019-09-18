def generate_population(pop_size=100, days_count=5):
    result = []
    for individual in range(pop_size):
        day = [1, 2, 3, 4, 5]
        days_in_schedule = []
        for day_index in range(days_count):
            days_in_schedule.append(day)

        result.append(days_in_schedule)

    return result


if __name__ == '__main__':
    population = generate_population()
    print('done')
