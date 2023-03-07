# Write a function called double_return
# It accepts a function and returns another function
# It should decorate a function by returning two copies of the inner function's return value inside a list
from functools import wraps


def double_return(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper(*args, **kwargs) returns the returned value from passed function twice inside a list."""
        return [func(*args, **kwargs)] * 2

    return wrapper


@double_return
def add(num1, num2):
    """add(number, number) returns the sum of the argument values."""
    return num1 + num2


@double_return
def greet(name):
    """greet(string) returns a string with the passed argument value embedded."""
    return f"Hi, I'm {name}"


# Test Code
print(add(5, 5))
print(add(45, 54))
print(greet("Colt"))
print(greet("Karishma"))
