import traceback
from contextlib import redirect_stdout
from datetime import datetime

from Task3 import decorator_3


class decorator_3_exception(decorator_3):
    def __init__(self, func):
        decorator_3.__init__(self, func)

    def __call__(self, *args, **kwds):
        try:
            func_res = decorator_3.__call__(self, *args, **kwds)
            return func_res
        except:
            with open("log.txt", "a") as f:
                with redirect_stdout(f):
                    print("Timestamp: ", datetime.now().timestamp())
                    print(traceback.format_exc(), "\n")
