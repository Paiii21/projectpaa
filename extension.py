import random
import time
import matplotlib.pyplot as plt

max_val = 250 - 88

def generate_array(n, max_val):
    return [random.randint(1, max_val) for _ in range(n)]

def check_uniqueness(array):
    return len(array) == len(set(array))

def measure_time(n_values, repeats=5):
    worst_case_times = []
    average_case_times = []

    random.seed(12345)  

    for n in n_values:
       
        array_worst_case = generate_array(n, max_val)
        while check_uniqueness(array_worst_case):
            array_worst_case = generate_array(n, max_val)  

       
        worst_case_duration = 0
        for _ in range(repeats):
            start_time = time.perf_counter()
            check_uniqueness(array_worst_case)
            end_time = time.perf_counter()
            worst_case_duration += (end_time - start_time)
        worst_case_times.append(worst_case_duration / repeats)

        array_average_case = generate_array(n, max_val)

        average_case_duration = 0
        for _ in range(repeats):
            start_time = time.perf_counter()
            check_uniqueness(array_average_case)
            end_time = time.perf_counter()
            average_case_duration += (end_time - start_time)
        average_case_times.append(average_case_duration / repeats)

    return worst_case_times, average_case_times

n_values = [100, 150, 200, 250, 300, 350, 400, 500]

worst_case_times, average_case_times = measure_time(n_values)

plt.plot(n_values, worst_case_times, label='Worst Case', marker='o')
plt.plot(n_values, average_case_times, label='Average Case', marker='x')

plt.xlabel('Size of Array (n)')
plt.ylabel('Time (seconds)')
plt.title('Worst Case vs Average Case Time Complexity')
plt.legend()
plt.grid(True)
plt.show()