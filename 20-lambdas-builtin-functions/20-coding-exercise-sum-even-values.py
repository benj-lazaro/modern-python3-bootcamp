# Write a function called sum_even_values
# Accepts a variable number of arguments
# Return the sum of arguments that are divisible by 2
# Otherwise return 0

def sum_even_values(*args):
    """sum_even_values(*args) returns the sum of argument values that are divisible by 2."""
    return sum(number for number in args if number % 2 == 0)


print("Function: sum_even_values()")
print(f"Documentation: {sum_even_values.__doc__}")

print("\nStatement: sum_even_values(1, 2, 3, 4, 5, 6)")
print(f"Result: {sum_even_values(1, 2, 3, 4, 5, 6)}")

print("\nStatement: sum_even_values(4, 2, 1, 10)")
print(f"Result: {sum_even_values(4, 2, 1, 10)}")

print("\nStatement: sum_even_values(1)")
print(f"Result: {sum_even_values(1)}")

print("\nStatement: sum_even_values(15)")
print(f"Result: {sum_even_values(15)}")

print("\nStatement: sum_even_values(24)")
print(f"Result: {sum_even_values(24)}")
