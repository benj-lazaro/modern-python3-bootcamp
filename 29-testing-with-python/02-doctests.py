# doctests
# Write tests for functions inside the docstring
# CATCH: Write code that looks like inside the Python REPL; it can be finicky to write tests
# To execute doctests in CLI: python3 -m doctest -v <filename.py>


def add(first_number, second_number):
    """add(number, number) returns the sum of the passed numerical argument values.
    >>> add(2, 3)
    5

    >>> add(100, 200)
    300
    """
    return first_number + second_number


# Test Code
print(f"add() documentation: {add.__doc__}")
print("Statement: add(25, 25)")
print(f"Result: {add(25, 25)}")
