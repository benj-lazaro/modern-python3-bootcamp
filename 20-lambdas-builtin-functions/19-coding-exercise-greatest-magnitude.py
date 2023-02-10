# Write a function called max_magnitude
# Accepts a single list full of numbers
# Returns the number with the largest magnitude that is furthest away from zero

def max_magnitude(list_data):
    """max_magnitude(list) return a number with the largest magnitude."""
    return max(abs(number) for number in list_data)

number_list_data_01 = [300, 20, -900]
number_list_data_02 = [10, 11, 12]
number_list_data_03 = [-5, -1, -89]

print("Function: max_magnitude(list)")
print(f"Documentation: {max_magnitude.__doc__}")
print(f"number_list_data_01: {number_list_data_01}")
print("Statement: max_magnitude(number_list_data_01)")
print(f"Result: {max_magnitude(number_list_data_01)}")

print(f"\nnumber_list_data_02: {number_list_data_02}")
print("Statement: max_magnitude(number_list_data_02)")
print(f"Result: {max_magnitude(number_list_data_02)}")

print(f"\nnumber_list_data_03: {number_list_data_03}")
print("Statement: max_magnitude(number_list_data_03)")
print(f"Result: {max_magnitude(number_list_data_03)}")
