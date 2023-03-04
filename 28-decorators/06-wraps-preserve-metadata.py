# Using wraps() to preserve a decorative function's metadata
from functools import wraps

def log_function_data(func):
    """log_function_data(function) calls and returns the passed function."""
    @wraps(func)  # Preserves the passed (decorated) function's attributes (e.g. __name__, __doc__)
    def wrapper(*args, **kwargs):
        """wrapper(*args, **kwargs) retuns the __name__ and __doc__ of the passed function."""
        print(f"You are about to call {func.__name__}")
        print(f"Here's the documentation: {func.__doc__}")
        return func(*args, **kwargs)

    return wrapper


@log_function_data
def add(number_1, number_2):
    """add(number, number) returns the sum of two numbers."""
    return number_1 + number_2


# Test Code
print(add(10, 40))
print("\n")
print(f"__name__: {add.__name__}")  # Access the Decorative function's __name__
print(f"__doc__: {add.__doc__}")    # Access the Decorative function's docstring
print("\nhelp():")
help(add)                           # Access the Decorative function's docstring using help()
