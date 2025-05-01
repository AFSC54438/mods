import time
from functools import wraps

def exe_time(f):
    in_progress = False

    @wraps(f)
    def wrapper(*args, **kwargs):
        nonlocal in_progress
        if in_progress:
            return f(*args, **kwargs)
        
        in_progress = True
        start = time.perf_counter()
        result = f(*args, **kwargs)
        end = time.perf_counter()
        in_progress = False

        print(f"Execution time ({f.__name__}): {(end - start)*1000:.5f} ms")
        return result
    return wrapper
