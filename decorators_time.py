import time

NUM_RUNS = 1000

class Timing:
    def __init__(self, func, num_runs = 100):
        self.start = 0
        self.num_runs = num_runs
        self.func = func
    def __enter__(self):
        self.start = time.time()
        return self
    def __exit__ (self, *args, **kwargs):
        avg_time = (time.time() - self.start) / self.num_runs
        print("Среднее время выполнения %.f" % (avg_time * 1_000_000), "мкс")

def res(param=1000):
    """функция для проверки работы декоратора"""
    for i in range(1, param):
        a = i**2

with Timing(res, NUM_RUNS) as ts:
    for i in range(NUM_RUNS):
        res()