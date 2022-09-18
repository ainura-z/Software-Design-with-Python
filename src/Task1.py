from contextlib import redirect_stdout
import time
import io


def decorator_1(func):
    """Print the function execution time and function call trace"""
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        start = time.perf_counter()
        with redirect_stdout(io.StringIO()) as f:
            func_res = func(*args, **kwargs)
        end = time.perf_counter()
        exec_time = end - start
        print(f"{func.__name__} call {wrapper.count} executed in %.5f sec" % exec_time)
        return func_res, f.getvalue()

    wrapper.count = 0
    return wrapper

