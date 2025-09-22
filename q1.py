
import numpy as np

def moving_average(data_list, window_size):
    result = []
    for i in range(len(data_list) - window_size + 1):
        window = data_list[i:i + window_size]
        avg = np.mean(window)
        result.append(round(avg, 2))
    return np.array(result)


    
