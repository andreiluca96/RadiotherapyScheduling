import texttable


def get_input():
    """Dummy method to be used just because it can do better formatting"""
    return {
        "classes": ["5A", "5B", "6A", "6B", "7A", "7B", "8A", "8B"],
        "teachers": [
            "Angel", "Alama", "Aragon", "Tifa", "Cloud",
            "Smokie", "Lucky", "Puffy", "Fluffy", "Roar",
            "Bonk", "Loki", "Titan", "Marcus", "Cazan"
        ],
        "assignments": [
            [
                0, 0, 0, 0, 0,
                1, 1, 1, 1, 1,
                2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7
            ], [
                9, 9, 9, 9, 9,
                10, 10, 10, 10, 10,
                2, 2, 3, 3, 4, 4, 5, 5, 8, 8, 7
            ], [
                0, 0, 0, 0, 0,
                1, 1, 1, 1, 1,
                2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7
            ], [
                9, 9, 9, 9, 9,
                10, 10, 10, 10, 10,
                2, 2, 3, 3, 4, 4, 5, 5, 8, 8, 7
            ], [
                0, 0, 0, 0, 0,
                1, 1, 1, 1, 1,
                2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7
            ], [
                9, 9, 9, 9, 9,
                10, 10, 10, 10, 10,
                2, 2, 3, 3, 4, 4, 5, 5, 8, 8, 7
            ], [
                0, 0, 0, 0, 0,
                1, 1, 1, 1, 1,
                2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7
            ], [9, 9, 9, 9, 9, 10, 10, 10, 10, 10, 2, 2, 3, 3, 4, 4, 5, 5, 8, 8, 7]
        ]
    }


def build_table_for_single_schedule(schedule, teachers):
    table = texttable.Texttable()
    table.add_row(["Slot", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
    for index in range(max([len(day) for day in schedule])):
        table.add_row(
            [index] + [teachers[schedule[day_index][index]] if index < len(schedule[day_index]) else '' for day_index in
                       range(5)])
    return table


def build_table_for_single_teacher(schedule, teacher, classes):
    table = texttable.Texttable()
    table.add_row(["Slot", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"])
    for slot_index in range(max([len(day) for class_schedule in schedule for day in class_schedule])):
        row = [f'{slot_index + 8}:00']
        for day_index in range(5):
            row_len = len(row)
            for class_index in range(len(schedule)):
                if len(schedule[class_index][day_index]) > slot_index and schedule[class_index][day_index][slot_index] == teacher:
                    row += [classes[class_index]]
            if row_len == len(row):
                row += ['']
        table.add_row(row)

    return table


def print_schedule(title, teachers, schedule):
    table = build_table_for_single_schedule(schedule, teachers)
    print('Class ' + title + '\n' + table.draw() + '\n')


def print_schedule_teacher(schedule, teacher, teachers, classes):
    table = build_table_for_single_teacher(schedule, teacher, classes)
    print(teachers[teacher] + '\n' + table.draw() + '\n')


if __name__ == '__main__':
    selected_individual = [[[0, 3, 4, 1], [0, 5, 0, 2], [2, 5, 6, 6, 1], [0, 1, 1, 1], [0, 3, 4, 7]],
                           [[5, 9, 10, 4, 10], [10, 9, 8, 9], [7, 10, 3, 5], [2, 10, 2, 3], [9, 9, 8, 4]],
                           [[3, 0, 1, 0], [2, 3, 5, 0], [6, 0, 2, 1], [7, 4, 0, 4, 1], [6, 1, 5, 1]],
                           [[9, 7, 8, 8], [9, 4, 10, 5], [4, 3, 9, 9], [3, 2, 9, 10, 10], [2, 5, 10, 10]],
                           [[6, 4, 2, 5, 0], [1, 0, 2, 1], [1, 6, 1, 4], [1, 3, 7, 0], [5, 0, 0, 3]],
                           [[2, 8, 3, 10, 3], [5, 8, 9, 4], [10, 9, 4, 10], [10, 9, 5, 9], [10, 7, 2, 9]],
                           [[1, 5, 0, 3], [6, 1, 1, 3], [5, 2, 0, 0], [4, 7, 4, 2], [1, 6, 1, 0, 0]],
                           [[4, 10, 9, 9], [7, 10, 4, 10], [3, 8, 10, 2], [9, 5, 10, 5, 9], [3, 2, 9, 8]]]
    input_data = get_input()
    for teacher_id in range(len(input_data['teachers'])):
        print_schedule_teacher(
            schedule=selected_individual,
            teacher=teacher_id,
            teachers=input_data['teachers'],
            classes=input_data['classes']
        )
