# Write a function called decrement_list
# Accepts a single parameter
# Returns a copy of the list where each item has been decremented by one


def decrement_list(list_data):
    """decrement_list(list) returns a list containing integer values decrement by 1."""
    return list(map(lambda item: item - 1, list_data))


print("Function: decrement_list()")
print(f"Documentation: {decrement_list.__doc__}")

test_data = [1, 2, 3, 4]
print(f"test_data: {test_data}")
print(f"Result: {decrement_list(test_data)}")

test_data = [10, 20, 30, 40]
print(f"test_data: {test_data}")
print(f"Result: {decrement_list(test_data)}")

