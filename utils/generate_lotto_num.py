import numpy as np
from datetime import datetime


def lotto_result():
    lotto_generated_data = np.random.choice(range(1, 46), 7, replace=False)
    lotto_generated_bonus = lotto_generated_data[-1]
    lotto_generated_data = lotto_generated_data[:-1]
    lotto_result_sorted = np.sort(lotto_generated_data)
    lotto_num_result = lotto_result_sorted.tolist()

    lotto_result = {
        "first": int(lotto_num_result[0]),
        "second": int(lotto_num_result[1]),
        "third": int(lotto_num_result[2]),
        "fourth": int(lotto_num_result[3]),
        "fifth": int(lotto_num_result[4]),
        "sixth": int(lotto_num_result[5]),
        "bonus": int(lotto_generated_bonus),
        "createAt": datetime.now().strftime("%Y-%m-%d")
    }
    return lotto_result


