import random
from functools import lru_cache


@lru_cache(maxsize=1)
def get_input(patients=250, days=15, slots=5, max_treatment_days=15):
    """Dummy method to be used just because it can do better formatting"""
    random.seed(7)
    return \
        {
            'patients': patients,
            'days': days,
            'slots': slots,
            'treatment_days': [random.randint(2, max_treatment_days) for _ in range(patients)],
            'priorities': [random.randint(1, 4) for _ in range(patients)]
        }


if __name__ == '__main__':
    input_data = get_input()
