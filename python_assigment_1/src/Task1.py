import io
import time
from contextlib import redirect_stdout


def decorator_1(func):
    """
    Prints the function execution time and function call trace.
    """

    def wrapper(*args, **kwds):
        wrapper.count += 1

        with redirect_stdout(io.StringIO()) as output:
            start = time.perf_counter()
            func_res = func(*args, **kwds)
            end = time.perf_counter()

        exec_time = end - start

        print(f"{func.__name__} call {wrapper.count} executed in {exec_time:.5f} sec.")

        return func_res, output.getvalue()

    wrapper.count = 0

    return wrapper
