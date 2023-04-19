# Write a function called find_the_duplicate()
# It accepts an array for numbers containing a single duplicate
# Returns the duplicate number
# Otherwise returns False


def find_the_duplicate(list_data):
    """find_the_duplicate(list) returns the single duplicate number in the list."""
    for item in range(len(list_data)):
        if list_data.count(list_data[item]) > 1:
            return list_data[item]


# Test Code
print(find_the_duplicate([1, 2, 1, 4, 3, 12]))      # Returns 1
print(find_the_duplicate([6, 1, 9, 5, 3, 4, 9]))    # Returns 9
print(find_the_duplicate([2, 1, 3, 4]))             # Returns None
