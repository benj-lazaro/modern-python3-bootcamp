# Write a function called range_in_list
# It accepts a list (containing integers), a start and end indices
# Returns the sum of values between the start & (including) end index
# If a start index is not passed, it defaults to 0
# If an end index is not passed, it defaults to the last element


def range_in_list(user_list, start_index=0, end_index=None):
    if end_index is None:
        return sum(user_list[start_index: len(user_list)])
    return sum(user_list[start_index: end_index + 1])


# Test Code
print(range_in_list([1, 2, 3, 4], 0, 2))    # Returns 6
print(range_in_list([1, 2, 3, 4]))          # Returns 10
print(range_in_list([2, 2]))                # Returns 4
print(range_in_list([1, 2, 3, 4], 0, 3))    # Returns 10
print(range_in_list([1, 2, 3, 4], 1))       # Returns 9
print(range_in_list([1, 2, 3, 4], 0, 100))  # Returns 10
print(range_in_list([], 0, 1))              # Returns 0
