# Write a function called sum_up_diagonals()
# It accepts an NxN list of lists
# Returns the sums up the two main diagonals in the array
# The one from the upper left to the lower right
# The one from the upper right to the lower left


def sum_up_diagonals(list_data):
    """sum_up_diagonals(list) returns the sum of two diagonal values of an NxN list."""
    first_diagonal_sum = sum(list_data[index][index] for index in range(len(list_data)))
    second_diagonal_sum = sum(list_data[index][len(list_data) - index - 1] for index in range(len(list_data)))
    return first_diagonal_sum + second_diagonal_sum


# Test Code
list_one = [
    [1, 2],
    [3, 4]
]
print(sum_up_diagonals(list_one))       # Returns 10

list_two = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(sum_up_diagonals(list_two))       # Returns 30

list_three = list3 = [
    [4, 1, 0],
    [-1, -1, 0],
    [0, 0, 9]
]
print(sum_up_diagonals(list_three))     # Returns 11

list_four = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
print(sum_up_diagonals(list_four))      # Returns 68
