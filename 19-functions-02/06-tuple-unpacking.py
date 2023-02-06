# Use * as an argument to 'unpack' list and tuple values

def sum_all_values(*args):
    """sum_all_values(*args) unpacks list/tuple argument items into items & returns the sum."""
    print(f"Argument values received: {args}")
    sum = 0

    for number in args:
        sum += number

    return sum


print("Function: sum_all_values()")
print(f"Documentation: {sum_all_values.__doc__}")
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
result = sum_all_values(*number_list)               # Pass argument value with * to unpack items
print(f"Sum: {result}")
