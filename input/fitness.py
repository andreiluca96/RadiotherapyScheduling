from input.utils import get_input


def fitness(candidate: [], input_data: {}):
    # timetable = [[0 for _ in range(input_data['slots'])]for _ in range(input_data['days'])]
    timetable = [[] for _ in range(input_data['days'])]
    # get patients in order
    fitness_value = 0
    current_attempted_priority = 1
    ok = True
    while ok:
        try:
            current_patient = candidate.index(current_attempted_priority)
            current_patient_days = input_data['treatment_days'][current_patient]
            # print(f'Scheduling patient with id {current_patient} which needs {current_patient_days} days')
            # allocate first day sessions
            for day_index, day in enumerate(timetable[:input_data['days'] - current_patient_days+1]):
                if len(day) <= input_data['slots'] - 2:
                    can_assign = True
                    # print(f'Patient {current_patient} can start on day {day_index}')
                    for next_day_index, next_day in enumerate(timetable[day_index + 1:day_index + current_patient_days]):
                        if len(next_day) == input_data['slots']:
                            # print(f'Day {next_day_index} does not have a free slot, cannot assign')
                            can_assign = False
                    if can_assign:
                        day.append(current_patient)
                        day.append(current_patient)
                        for next_day in timetable[day_index + 1:day_index + current_patient_days]:
                            next_day.append(current_patient)
                        fitness_value += 12 / input_data['priorities'][current_patient]
                        break
            current_attempted_priority += 1
        except ValueError:
            ok = False
    return fitness_value
    # print(timetable)
    # print(fitness_value)


if __name__ == '__main__':
    input_data = get_input()
    print(input_data)
    fitness([2, 4, 1, 5, 3], input_data)
    fitness([1, 2, 3, 4, 5], input_data)
    fitness([5, 4, 3, 2, 1], input_data)
