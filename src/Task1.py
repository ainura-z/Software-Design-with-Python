import contextlib
import time
import io

def decorator_1(func):
    """Print the function execution time and function call trace"""
    def wrapper_time_call(*args, **kwargs):
        start = time.perf_counter()
        wrapper_time_call.count += 1
        with contextlib.redirect_stdout(io.StringIO()) as f:
            func(*args, **kwargs)
        end = time.perf_counter()
        exec_time = end - start
        print(f"{func.__name__} call {wrapper_time_call.count} executed in %.5f sec" % exec_time)# round(exec_time, 5)

    wrapper_time_call.count = 0
    return wrapper_time_call


