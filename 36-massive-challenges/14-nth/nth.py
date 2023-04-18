# Write a function called nth()
# It accepts a list and an integer
# Returns the element at whatever index is the number (integer) in the list
# If the integer is negative, the nth element from the end of the list is returned

def nth(list_data, index):
    """nth(list, int) returns the corresponding list item based on the passed index value."""
    return list_data[index]


# Test Code
print(nth(['a', 'b', 'c', 'd'], 1))     # Returns 'b'
print(nth(['a', 'b', 'c', 'd'], -2))    # Returns 'c'
print(nth(['a', 'b', 'c', 'd'], 0))     # Returns 'a'
print(nth(['a', 'b', 'c', 'd'], -4))    # Returns 'a'
print(nth(['a', 'b', 'c', 'd'], -1))    # Returns 'd'
print(nth(['a', 'b', 'c', 'd'], 3))     # Returns 'd'
