import random
from functools import lru_cache


@lru_cache(maxsize=1)
def get_input():
    """Dummy method to be used just because it can do better formatting"""

    patients = 100
    days = 20
    slots = 10
    random.seed(7)
    return \
        {
            'patients': patients,
            'days': days,
            'slots': slots,
            'treatment_days': [random.randint(2, 5) for _ in range(patients)],
            'priorities': [random.randint(1, 4) for _ in range(patients)]
        }

#
# def build_table_for_single_schedule(schedule, teachers):
#     table = texttable.Texttable()
#     table.add_row(["Slot", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
#     for index in range(max([len(day) for day in schedule])):
#         table.add_row(
#             [index] + [teachers[schedule[day_index][index]]
#             if index < len(schedule[day_index]) else '' for day_index in
#                        range(5)])
#     return table
#
#
# def build_table_for_single_teacher(schedule, teacher, classes):
#     table = texttable.Texttable()
#     table.add_row(["Slot", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
#     for slot_index in range(max([len(day) for class_schedule in schedule for day in class_schedule])):
#         row = [f'{slot_index + 8}:00']
#         for day_index in range(5):
#             added_character = ''
#             for class_index in range(len(schedule)):
#                 if len(schedule[class_index][day_index]) > slot_index \
#                 and schedule[class_index][day_index][slot_index] == teacher:
#                     added_character = classes[class_index]
#             row += [added_character]
#         table.add_row(row)
#
#     return table
#
#
# def print_schedule(title, teachers, schedule):
#     table = build_table_for_single_schedule(schedule, teachers)
#     print('Class ' + title + '\n' + table.draw() + '\n')
#
#
# def print_schedule_teacher(schedule, teacher, teachers, classes):
#     table = build_table_for_single_teacher(schedule, teacher, classes)
#     print(teachers[teacher] + '\n' + table.draw() + '\n')


if __name__ == '__main__':
    input_data = get_input()

