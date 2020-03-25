from time import perf_counter


def timer(num_trails, call_func, *args, **kwargs):
    start = perf_counter()
    for i in range(num_trails):
        call_func(*args, **kwargs)
    end = perf_counter()
    thresh_avg_time = float(end - start) / num_trails
    return thresh_avg_time
