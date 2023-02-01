# docstring = documenting functions; essential when writing complex functions
def say_hello():
    """A simple function that returns the string hello"""
    return "Hello!"


def exponent(number, power=2):
    """The exponent(number, power) raises number to specified power. Power defaults to 2."""
    return number ** power


# Display docstring of defined functions
print(f"say_hello() docstring: {say_hello.__doc__}")
print(f"exponent() docstring: {exponent.__doc__}")
