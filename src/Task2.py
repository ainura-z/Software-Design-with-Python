from Task1 import decorator_1
from inspect import signature, getdoc, getsource
import textwrap


def decorator_2(func):
    """
    Print the function execution time,
    function call trace and original source code of the function
    """
    def wrapper(*args, **kwargs):
        func_res, output = decorator_1(func)(*args, **kwargs)
        ind = 10
        print("Name:".ljust(ind), func.__name__)
        print("Type:".ljust(ind), type(func))
        print("Sign:".ljust(ind), signature(func))
        print("Args:".ljust(ind), "positional", args)
        print(" ".ljust(ind), "key=worded", kwargs, '\n')

        doc = textwrap.indent(text=getdoc(func), prefix=(ind+1)*' ')[ind+1:]
        print("Doc:".ljust(ind), doc, '\n')

        source = textwrap.indent(text=getsource(func), prefix=(ind+1)*' ')[ind+1:]
        print("Source:".ljust(ind), source)

        output = textwrap.indent(text=output, prefix=(ind+1)*' ')[ind+1:]
        print("Output:".ljust(ind), output, '\n')

        return func_res

    return wrapper

