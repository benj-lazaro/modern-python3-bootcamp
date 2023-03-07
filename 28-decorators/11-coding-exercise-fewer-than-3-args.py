# Write a function called ensure_fewer_than_3_args
# Accepts a function and returns another function
# The passed function should ONLY be invoked if there are less than 3 positional arguments
# Otherwise, the inner function should return "Too many arguments!"
from functools import wraps


def ensure_fewer_than_3_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper(*args, **kwargs) check if args is < 3 in order to execute the passed function."""
        if len(args) < 3:
            return func(*args, **kwargs)
        else:
            return "Too many arguments!"

    return wrapper


@ensure_fewer_than_3_args
def add_all(*numbers):
    """add_all(*numbers) returns the sum of argument values of numbers."""
    return sum(numbers)


# Test Code
print(add_all(1))           # Returns 1
print(add_all(1, 2))        # Returns 3
print(add_all(47, 74))      # Returns 121
print(add_all(1.1, 2.2))    # Returns 3.300000000000003
print(add_all(1, 2, 3))     # Triggers the string 'Too many arguments!'
