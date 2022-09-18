from contextlib import redirect_stdout
import time
import io
from inspect import signature, getdoc, getsource
import textwrap

rank = {}


class decorator_3:
    """
    Print the function execution time,
    function call trace and original source code of the function
    """
    def __init__(self, func):
        self.func = func
        self.count = 0
        self.time = 0.0

    def __call__(self, *args, **kwargs):
        self.count += 1

        with redirect_stdout(io.StringIO()) as f:
            start = time.perf_counter()
            func_res = self.func(*args, **kwargs)
            end = time.perf_counter()
            output = f.getvalue()

        self.time = end - start
        rank[self.func.__name__] = round(self.time, 5)

        ind = 10
        with open('output.txt', 'a') as file:
            file.write(f"{self.func.__name__} call {self.count} executed in %.5f sec \n" % self.time)

            file.write("Name:".ljust(ind) + str(self.func.__name__) + '\n')
            file.write("Type:".ljust(ind) + str(type(self.func)) + '\n')
            file.write("Sign:".ljust(ind) + str(signature(self.func)) + '\n')
            file.write("Args:".ljust(ind) + "positional" + str(args) + '\n')
            file.write(" ".ljust(ind) + "key=worded" + str(kwargs) + '\n\n')

            doc = textwrap.indent(text=getdoc(self.func), prefix=ind * ' ')[ind:]
            file.write("Doc:".ljust(ind) + doc + '\n\n')

            source = textwrap.indent(text=getsource(self.func), prefix=ind * ' ')[ind:]
            file.write("Source:".ljust(ind) + source + '\n\n')

            out = textwrap.indent(text=output, prefix=ind * ' ')[ind:]
            file.write("Output:".ljust(ind) + out + '\n\n')

        return func_res


def plot_rank():
    rank_df = dict(sorted(rank.items(), key=lambda item: item[1]))
    print("Program".ljust(30), "|".ljust(6), "Rank".ljust(5), "|".ljust(6), "Time Elapsed")
    for i, key_value in enumerate(rank_df.items()):
        print(key_value[0].ljust(38), i+1, " ".ljust(12), key_value[1])
