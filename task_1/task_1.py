import numpy as np


hist_list = [0] * 10
data_list = np.random.randint(0, 1000, size=1000000)

for data in data_list:
    hist_list[data // 100] += 1
