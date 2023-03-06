# Another use case of Decorators is to enforce certain restrictions on arguments
from functools import wraps

def ensure_no_kwargs(func):
    """ensure_no_kwargs(function) calls and returns the wrapper()."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper(*args, **kwargs) checks for passed kwargs and raises a ValueEror if there is one."""
        if kwargs:
            raise ValueError("No keyword arguments (kwargs) allowed! Sorry.")

        return func(*args, **kwargs)
    return wrapper


@ensure_no_kwargs
def greet(name):
    """greet(string) returns a string containing the passed argument value."""
    print(f"Hi there {name}!")


greet("Haruna")
greet(name="Iikubo")    # Raises a ValueError defined within the Decorator ensure_no_kwargs()
