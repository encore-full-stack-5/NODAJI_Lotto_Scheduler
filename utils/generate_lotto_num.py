import numpy as np
from datetime import datetime


def lotto_result():
    lotto_generated_data = np.random.choice(range(1, 46), 6, replace=False)
    lotto_generated_bonus = np.random.randint(1, 46)
    lotto_result_sorted = np.sort(lotto_generated_data)
    lotto_num_result = lotto_result_sorted.tolist()

    lotto_result = {
        "first_number": lotto_num_result[0],
        "second_number": lotto_num_result[1],
        "third_number": lotto_num_result[2],
        "fourth_number": lotto_num_result[3],
        "fifth_number": lotto_num_result[4],
        "sixth_number": lotto_num_result[5],
        "bonus_number": lotto_generated_bonus,
        "create_at": datetime.now().strftime("%Y-%m-%d")
    }
    return lotto_result


