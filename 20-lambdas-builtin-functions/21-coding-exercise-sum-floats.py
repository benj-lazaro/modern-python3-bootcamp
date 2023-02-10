# Write a function called sum_floats
# Accepts a variable number of arguments
# Retuns the sum of argument values that are floats
# Otherwise, return 0

def sum_floats(*args):
    """sum_floats(*args) returns the sum of argument values that are floats, otherwise return 0."""
    return sum(number for number in args if type(number) == float)


print("Function: sum_floats()")
print(f"Documentation: {sum_floats.__doc__}")

print("\nStatement: sum_floats(1.0, 1.0)")
print(f"Result: {sum_floats(1.0, 1.0)}")

print("\nStatement: sum_floats(1, 10.0)")
print(f"Result: {sum_floats(1, 10.0)}")

print("\nStatement: sum_floats(1, 2, 3, 4, 5)")
print(f"Result: {sum_floats(1, 2, 3, 4, 5)}")

print("\nStatement: sum_floats('you', 'are', 'awesome', 4.0, 5.0)")
print(f"Result: {sum_floats('you', 'are', 'awesome', 4.0, 5.0)}")
