import time

def time_this(num_runs=10):
    def decorator(func_to_run):
        def func(*args, **kwargs):
            avg = 0
            for _ in range(num_runs):
                t0 = time.time()
                func_to_run(*args, **kwargs)
                t1 = time.time()
                avg += (t1 - t0)
            avg /= num_runs
            fn = func_to_run.__name__
            print("Среднее время выполнения %s за %s запусков: %.5f" % (fn, num_runs, avg))
        return func

    return decorator

@time_this(num_runs=10)
def f():
    for j in range(1000000):
        pass
f()
