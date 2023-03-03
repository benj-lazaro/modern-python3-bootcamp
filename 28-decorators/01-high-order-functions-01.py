# High Order Function is A regular function that:
# - Returns a function
# - Accepts one or more functions as an argument
# - Pass functions as arguments to other functions

def sum(number, func):
    """sum(int, function) returns the sum of the passed integer value & called function."""
    total = 0

    for num in range(1, number + 1):
        total += func(num)

    return total


def square(number):
    """square(int) returns the squared value of the passed integer value."""
    return number * number


def cube(number):
    """cube(int) returns the cubed value of the passed integer value."""
    return number * number * number


print("Statement: sum(3, square)")
print(f"Result: {sum(3, square)}")

print("\nStatement: sum(3, cube)")
print(f"Result: {sum(3, cube)}")
