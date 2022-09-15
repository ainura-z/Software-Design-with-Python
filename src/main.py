from Task1 import decorator_1
from Task2 import decorator_2
import random

@decorator_2
def func_1():
    """
    I am ready to Start
    dvszdv
    """
    result = 0
    n = random.randint(10, 751)
    for i in range(n):
        result += (i ** 2)


@decorator_2
def func_2(n=2, m=5):
    print("I am ready to do serious stuff")
    max_val = float('-inf')
    n = random.randint(10,751)
    res = [pow(i,2) for i in range(n)]
    for i in res:
        if i > max_val:
            max_val = i


if __name__ == '__main__':
    func_1()
    # func_1()
    func_2()
