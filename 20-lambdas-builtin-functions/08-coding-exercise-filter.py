# Write a function called remove_negatives
# Accepts a list of numbers
# Returns a copy of the list with all negative numbers removed

def remove_negatives(list_data):
    """remove_negatives(list) returns a list with all negative numbers removed."""
    return list(filter(lambda number: number >= 0, list_data))


print("Function: remove_negatives()")
print(f"Documentation: {remove_negatives.__doc__}")
number_list = [-7, 0, 1, 2, 3, 4, 5]
print(f"number_list: {number_list}")
print(f"Result: {remove_negatives(number_list)}")

number_list = [-1, 3, 4, -99]
print(f"number_list: {number_list}")
print(f"Result: {remove_negatives(number_list)}")
