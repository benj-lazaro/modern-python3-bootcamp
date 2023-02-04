# *args = special operator passed into a function as a parameter in the form of a tuple
# def <function_name){*<parameter_name):

def sum_all_numbers(*args):
    """sum_alL_numbers(*args) returns the sum of passed argument values (integer)."""
    sum = 0
    for number in args:
        sum += number

    return sum


def ensure_correct_information(*args):
    """ensure_correct_information(*args) check argument values and return corresponding message."""
    if "Colt" in args and "Steele" in args:
        return "Welcome back Colt!"

    return "Not sure who you are..."


print("Function: sum_all_numbers()")
print(f"Documentation: {sum_all_numbers.__doc__}")
print(f"Sum of numbers 1 to 3: {sum_all_numbers(1, 2, 3)}")
print(f"Sum of numbers 1 to 10: {sum_all_numbers(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)}")

print("\nFunction: ensure_correct_information()")
print(f"Documentation: {ensure_correct_information.__doc__}")
print(f"Result: {ensure_correct_information(1, True, 'Steele', 'Colt', 'Tesla', 'Bezoes')}")
print(f"Result: {ensure_correct_information('Colt', 'Andy', 'Bud')}")
print(f"Result: {ensure_correct_information()}")
