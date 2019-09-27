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


def print_schedule(title, teachers, schedule):
    table = build_table_for_single_schedule(schedule, teachers)
    print('Class ' + title + '\n' + table.draw() + '\n')

