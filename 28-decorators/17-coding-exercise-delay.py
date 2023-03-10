# Write a function called delay
# It accepts time and returns an inner function that accepts a function
# delay() will wait to execute by the amount of time passed into it
# delay() will display a message to inform the user of the delay before the decorated function gets called
# Hint: Use the sleep() to pause the code execution for a certain amount of time

from functools import wraps
from time import sleep

def delay(time):
    """dalay(int) accepts the passed numerical argument value that will be used by sleep() & calls inner()."""
    def inner(func):
        """inner(func) accepts passed function and calls wrapper()."""
        @wraps(func)
        def wrapper(*args, **kwargs):
            """wrapper(*args, **kwargs) prints a string, pause execution and then return the passed function."""
            print("Waiting " + str(time) + "s before running " + func.__name__ +"()...")
            sleep(time)
            return func(*args, **kwargs)
        return wrapper
    return inner


@delay(3)
def say_hello():
    """say_hello() returns a string."""
    return "Well, hello there."


# Test Code
print(say_hello())
