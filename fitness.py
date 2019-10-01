def fitness(candidate):
    fitness_score = 0
    for day_index in range(5):
        for hour_index in range(7):
            ids = []
            for class_group in candidate:
                try:
                    ids.append(class_group[day_index][hour_index])
                except:
                    pass
            if len(ids) == len(set(ids)):
                fitness_score += 1
    return fitness_score