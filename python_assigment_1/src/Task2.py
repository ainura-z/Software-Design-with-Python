import textwrap
from inspect import getdoc, getsource, signature

from Task1 import decorator_1

column = 10


def decorator_2(func):
    """
    Prints the function execution time,
    function call trace and the original source code of the function.
    """

    def wrapper(*args, **kwds):
        func_res, output = decorator_1(func)(*args, **kwds)

        print("Name:".ljust(column), func.__name__)
        print("Type:".ljust(column), type(func))
        print("Sign:".ljust(column), signature(func))
        print("Args:".ljust(column), "positional", args)
        print("".ljust(column), "key=worded", kwds, "\n")

        doc = textwrap.indent(text=getdoc(func), prefix=(column + 1) * " ")[
            column + 1 :
        ]
        print("Doc:".ljust(column), doc, "\n")

        source = textwrap.indent(text=getsource(func), prefix=(column + 1) * " ")[
            column + 1 :
        ]
        print("Source:".ljust(column), source)

        output = textwrap.indent(text=output, prefix=(column + 1) * " ")[column + 1 :]
        print("Output:".ljust(column), output, "\n")

        return func_res

    return wrapper
