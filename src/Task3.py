import io
import textwrap
import time
from contextlib import redirect_stdout
from inspect import getdoc, getsource, signature

rank = {}
column = 10


class decorator_3:
    """
    Prints the function execution time,
    function call trace and the original source code of the function.
    """
    def __init__(self, func):
        self.func = func
        self.count = 0
        self.exec_time = 0.0

    def __call__(self, *args, **kwds):
        self.count += 1

        with redirect_stdout(io.StringIO()) as output:
            start = time.perf_counter()
            func_res = self.func(*args, **kwds)
            end = time.perf_counter()

        self.exec_time = end - start

        rank[self.func.__name__] = round(self.exec_time, 5)

        with open("output.txt", "a") as output_file:
            output_file.write(
                f"{self.func.__name__} call {self.count} executed in {self.exec_time:.5f} sec.\n"
            )

            output_file.write("Name:".ljust(column) + str(self.func.__name__) + "\n")
            output_file.write("Type:".ljust(column) + str(type(self.func)) + "\n")
            output_file.write("Sign:".ljust(column) + str(signature(self.func)) + "\n")
            output_file.write("Args:".ljust(column) + "positional" + str(args) + "\n")
            output_file.write(" ".ljust(column) + "key=worded" + str(kwds) + "\n\n")

            doc = textwrap.indent(text=getdoc(self.func), prefix=column * " ")[column:]
            output_file.write("Doc:".ljust(column) + doc + "\n\n")

            source = textwrap.indent(text=getsource(self.func), prefix=column * " ")[
                column:
            ]
            output_file.write("Source:".ljust(column) + source + "\n\n")

            out = textwrap.indent(text=output.getvalue(), prefix=column * " ")[column:]
            output_file.write("Output:".ljust(column) + out + "\n\n")

        return func_res


def plot_rank():
    rank_df = dict(sorted(rank.items(), key=lambda item: item[1]))
    print(
        "Program".ljust(30), "|".ljust(6), "Rank".ljust(5), "|".ljust(6), "Time Elapsed"
    )
    for i, key_value in enumerate(rank_df.items()):
        print(key_value[0].ljust(38), i + 1, " ".ljust(12), key_value[1])
