# Write a function called once()
# It accepts a function
# Returns a new function that can only be invoked ONCE
# If the said function is invoked more than once, it should return None


def add(first_number, second_number):
    """add(int, int) returns the sum of the passed 2 numbers."""
    return first_number + second_number


def subtract(first_number, second_number):
    """subtract(int, int) returns the difference o the passed 2 numbers."""
    return first_number - second_number


def once(function):
    """once(function) ensures that the passed function is invoked once."""
    call_count = 0

    def inner_function(*args):
        nonlocal call_count

        if call_count == 0:
            call_count += 1
            return function(*args)
        return None

    return inner_function


# Test Code
add_once = once(add)
print(add_once(1, 2))
print(add_once(5, 3))

subtract_once = once(subtract)
print(subtract_once(5, 3))
print(subtract_once(10, 3))
