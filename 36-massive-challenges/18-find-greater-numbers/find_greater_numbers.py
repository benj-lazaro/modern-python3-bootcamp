# Write a function called find_greater_numbers()
# It accepts a list of integers
# Returns the number of times an integer is followed by a larger integer across the entire list


def find_greater_numbers(list_data):
    """find_greater_number(list) returns the number of times an integer is followed by a greater number."""
    counter = 0
    for predecessor_index in range(len(list_data)):
        # Check if current integer value is followed by an integer of higher value
        for successor_index in range(predecessor_index, len(list_data)):
            if list_data[predecessor_index] < list_data[successor_index]:
                counter += 1

    return counter


print(find_greater_numbers([1, 2, 3]))          # Returns 3
print(find_greater_numbers([6, 1, 2, 7]))       # Returns 4
print(find_greater_numbers([5, 4, 3, 2, 1]))    # Returns 0
print(find_greater_numbers([]))                 # Return 0
