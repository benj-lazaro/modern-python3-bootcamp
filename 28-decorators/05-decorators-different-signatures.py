# Decorators with different/multiple signatures (arguments) demo

def shout(func):
    """shout(function) executes and retuns the wrapper() function."""
    def wrapper(*args, **kwargs):
        """wrapper(*args, **kwargs) calls and returns the passed function & argument value(s)."""
        return func(*args, **kwargs).upper()
    return wrapper


@shout
def greet(name):
    """greet(str) accepts a string and returns a formatted string."""
    return f"Hi, I'm {name}."


@shout
def order(main, side):
    """order(str, str) accetps two strings and returns a formatted string."""
    return f"Hi, I'd like the {main}, with a side of {side}, please."


@shout
def lol():
    """lol() returns a string."""
    return f"lol"


# Test Code
print(greet("Sayumi"))

print(order("burger", "fries"))
print(order(side="burger", main="fries"))

print(lol())
