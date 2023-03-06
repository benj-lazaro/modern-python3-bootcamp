# Write a function called show_args
# It accepts a function and returns another function
# Before invoking the passed function, it should be able to:
# - Print a tuple of the positional arguments
# - Print a dictionary of keyword arguments
from functools import wraps
def show_args(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper(*args, **kwargs) prints the *args and/or **kwargs of the passed function."""
        print(f"Here are the args: {args}")
        print(f"Hwere are the kwargs: {kwargs}")
        result = func()
        return result
    return wrapper


@show_args
def do_nothing(*args, **kwargs):
    """do_nothing(*args, **kwargs) does nothing."""
    pass


print("Statement: do_nothing(1, 2, 3,a='hi', b='bye')")
do_nothing(1, 2, 3,a="hi",b="bye")
