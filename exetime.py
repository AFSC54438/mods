import time

def exe_time(f):
    def wrapper():
        start = time.perf_counter()
        f()
        end = time.perf_counter()
        print(f"Execution time ({f.__name__}): {(end - start)*1000} ms")
    return wrapper
