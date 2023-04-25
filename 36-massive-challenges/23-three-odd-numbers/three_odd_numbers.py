# Write a function called three_odd_numbers()
# It accepts a list of integers
# Returns True if three consecutive integers sum up to an odd integer


def three_odd_numbers(number_list):
    """three_odd_numbers(list) returns True if any 3 integers sum up to an odd number."""
    for index in range(len(number_list) - 2):
        # Fetch 3 integers from the list and sum up them
        sum_total = sum(number_list[index: index + 3])

        # Odd number check
        if sum_total % 2 == 1:
            return True

    return False


# Test Code
print(three_odd_numbers([1, 2, 3, 4, 5]))                   # Returns True
print(three_odd_numbers([1, 2]))                            # Returns False
print(three_odd_numbers([0, -2, 4, 1, 9, 12, 4, 1, 0]))     # Returns True
print(three_odd_numbers([5, 2, 1]))                         # Returns False
print(three_odd_numbers([1, 2, 3, 3, 2]))                   # Returns False
