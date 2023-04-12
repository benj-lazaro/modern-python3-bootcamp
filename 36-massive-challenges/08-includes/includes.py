# Write a function called includes()
# Accepts a collection, a value and an optional starting index
# Returns True if the value exists in the collection when searching using the starting index
# Otherwise return False


def includes(collection, search_value, start_index=0):
    """includes(collection, str, int) returns True if the search_value exists within the colleciton"""
    if isinstance(collection, dict):
        if search_value in collection.values():
            return True
    else:
        for item in range(start_index, len(collection)):
            if collection[item] == search_value:
                return True
    return False


# Test Code
print(includes([1, 2, 3], 1))  # True
print(includes([1, 2, 3], 1, 2))  # False; starting from index 2, search for the value of 1
print(includes({'a': 1, 'b': 2}, 1))  # True
print(includes({'a': 1, 'b': 2}, 'a'))  # False; search for the value of 'a', NOT key of 'a'
print(includes('abcd', 'b'))  # True
print(includes('abcd', 'e'))  # False; value of 'e' is non-existent in the collection
