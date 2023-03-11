from functools import wraps
from time import perf_counter
def measure(func):
    @wraps(func)
    def _time_it(*args, **kwargs):
        start = perf_counter()
        try:
            return func(*args, **kwargs)
        finally:
            end_ = perf_counter() - start
            print(f"Total execution time: {end_ if end_ > 0 else 0} s")
    return _time_it
