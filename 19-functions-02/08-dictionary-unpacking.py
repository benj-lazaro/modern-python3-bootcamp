# Use ** as an argument to 'unpack' dictionary values

def display_names(first, second):
    """display_names(first, second) unpacks dictionary items and returns a string."""
    print(f"Argument value received: {first} {second}")
    return f"{first} says hello to {second}"


def add_and_multiply_numbers(a, b, c):
    """add_and_multiply_numbers(a, b, c) unpacks dictionary items, retuns the product & sum of arguments a, b & c."""
    print(f"Argument value received: {a} {b} {c}")
    return a + b * c

name_dictionary = {
    "first": "Colt",
    "second": "Rusty"
}

number_dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}

print("Function: display_names()")
print(f"Documentation: {display_names.__doc__}")
print(f"Result: {display_names(**name_dictionary)}")

print("\nFunction: add_multiply_numbers()")
print(f"Documentation: {add_and_multiply_numbers.__doc__}")
print(f"Result: {add_and_multiply_numbers(**number_dictionary)}")
