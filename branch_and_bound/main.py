import time
from copy import deepcopy

from input.fitness import fitness
from input.utils import get_input


def fitness_and_last_patient(candidate: [], input_data: {}):
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
            for day_index, day in enumerate(timetable[:input_data['days'] - current_patient_days + 1]):
                if len(day) <= input_data['slots'] - 2:
                    can_assign = True
                    # print(f'Patient {current_patient} can start on day {day_index}')
                    for next_day_index, next_day in enumerate(
                            timetable[day_index + 1:day_index + current_patient_days]):
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
    return fitness_value, current_patient


max_value = 0
best_fit = []


def branch_and_bound(list, left, right, input_data):
    global max_value
    global best_fit
    if left == right:
        fitness, last_patient = fitness_and_last_patient(list, input_data)
        if max_value < fitness:
            max_value = fitness
            best_fit = deepcopy(list)
        # print(f'{list}, {fitness}, {last_patient}')
    else:
        for i in range(left, right + 1):
            fitness, last_patient = fitness_and_last_patient(list, input_data)
            if max(list[left:right]) > last_patient + 1:
                break
            list[left], list[i] = list[i], list[left]
            branch_and_bound(list, left + 1, right, input_data)
            list[left], list[i] = list[i], list[left]  # backtrack


if __name__ == '__main__':
    data = get_input(patients=11)

    start_time = time.time()
    initial_solution = range(1, data['patients'])
    n = len(initial_solution)
    a = list(initial_solution)
    branch_and_bound(a, 0, n - 1, data)

    print(f'{max_value}, {best_fit}')
    print(time.time() - start_time)
