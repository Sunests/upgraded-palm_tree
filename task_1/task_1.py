import numpy as np
import time


def calc_hist():
    hist_list = [0] * 10
    data_list = np.random.randint(0, 1000, size=1000000)

    for data in data_list:
        hist_list[data // 100] += 1


def execution_time_calc_hist():
    start = time.time()
    calc_hist()
    end = time.time()
    return end - start


time_list = [execution_time_calc_hist() for i in range(100)]

print('max time ->', max(time_list))
print('min time ->', min(time_list))
print('mean time ->', sum(time_list) / 100)
