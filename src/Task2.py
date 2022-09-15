from Task1 import decorator_1
import contextlib
import time
import io
from inspect import signature
from inspect import getargspec

def decorator_2(func):
    def wrapper_time_call(*args, **kwargs):
        dec_1 = decorator_1(func)(*args, **kwargs)

        print("Name:".ljust(6), func.__name__)
        print("Type:".ljust(6), type(func))
        print("Sign:".ljust(6), signature(func))
        print("Args".ljust(6), args)
        print(" ".ljust(10), kwargs)
        # print(f"{'Args:': <20}positional {args}")
        # print(f"{'': <20}keyworded {kargs}")

        # print("Doc:".ljust(6), func.__doc__.splitlines())
        print("Output:".ljust(6), dec_1.getvalue())

    return wrapper_time_call
