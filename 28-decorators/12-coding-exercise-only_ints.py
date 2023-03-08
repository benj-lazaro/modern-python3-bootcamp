# Write a function called only_ints
# It accepts a function and returns another function
# The passed function should ONLY be invoked if the argument values are integers
# Otherwise, the inner function returns a string "Please only invoke with integers"
from functools import wraps


def only_ints(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper(*args, **kwargs) returns the passed function ONLY if the argument values are integers."""
        if any([arg for arg in args if type(arg) != int]):
            return "Please only invoke with integers."
        return func(*args, **kwargs)

    return wrapper


@only_ints
def add(x, y):
    """add(int, int) returns the sum of passed argument values."""
    return x + y


# Test Code
print(add(1, 1))
print(add(1.1, 1))
print(add(1, 1.1))
