import time

def exe_time(f):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = f(*args, **kwargs)
        end = time.perf_counter()
        print(f"Execution time ({f.__name__}): {(end - start)*1000:.5f} ms")
        return result
    return wrapper
