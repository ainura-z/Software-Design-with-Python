from Task1 import decorator_1
from Task2 import decorator_2
from Task3 import decorator_3, plot_rank
from Task4 import decorator_1_error, decorator_3_error
from math import sqrt


@decorator_1
def sort_list_of_tuples(lst):
    """This function is sorting list of tuples"""
    print(f"Original list of tuples:{lst}")
    lst.sort(key=lambda x: x[1])
    print(f"Sorted List of Tuples:{lst}")
    return lst


@decorator_1
def palindromes(lst):
    """
    This function is looking for
    palindromes in a given list of strings
    """
    result = list(filter(lambda s: s == s[::-1], lst))
    print("List of palindromes:")
    print(result)


@decorator_1
def pascal_triangle(n):
    """ This function prints the Pascal's triangle (n+1) layers"""

    if n < 0:
        print("Input a number greater than 0")
        raise Exception("n cannot be less than 0")

    row = [1]
    for i in range(n+1):
        print(row)
        row = [sum(x) for x in zip([0] + row, row + [0])]


@decorator_1
def quadratic_equation_solver(a, b, c=1):
    """
    This function solves a quadratic
    equation a*x^2 + b*x + c = 0
    and print the result
    """
    if a == 0:
        print("This is a linear equation")
        raise ZeroDivisionError("a cannot be 0")
    # calculating the discriminant
    discriminant = b*b - 4*a*c
    # calculating the root of discriminant
    sqrt_discriminant = sqrt(abs(discriminant))
    # considering 3 cases
    if discriminant > 0:
        x1 = (-b + sqrt_discriminant)/(2*a)
        x2 = (-b - sqrt_discriminant)/(2*a)
        print("D>0:\nTwo real roots:")
        print(f"x1 = {x1} \nx2 = {x2}")
    elif discriminant == 0:
        x = -b/2*a
        print("D=0:\nOne real root:")
        print("x = ", x)
    else:
        x1_real = - b / (2 * a)
        x1_imaginary = sqrt_discriminant/(2*a)
        print("D<0:\nTwo complex roots:")
        print(f"x1 = {x1_real} + i*{x1_imaginary:.4f} \nx2 = {x1_real} - i*{x1_imaginary:.4f}")


if __name__ == '__main__':
    name_age = [('Alex', 20), ('Kris', 65), ('Amanda', 30), ('David', 45)]
    palindrome_list = ['aba', 'aaa', 'bba', 'a']

    # Task1, Task2
    sort_list_of_tuples(name_age)
    pascal_triangle(0)
    pascal_triangle(1)
    quadratic_equation_solver(1, 1, 1)
    palindromes(palindrome_list)
    quadratic_equation_solver(5, 0, c=2)
    pascal_triangle(10)

    # Task3
    # plot_rank()

    # Task4
    # pascal_triangle(-1)
    # quadratic_equation_solver(0, 1, 1)
