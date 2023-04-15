# Write a function called includes()
# Accepts a collection, a value to search within the collection and an optional starting index
# Returns True if the value exists w/in the collection, (optionally) starting from the starting index
# Otherwise return False


def includes(collection, search_value, start_index=None):
    """includes(collection, str, int) returns True if the search_value exists within the collection"""
    if type(collection) == dict:
        return search_value in collection.values()
    if start_index is None:
        return search_value in collection
    return search_value in collection[start_index:]


# Test Code
print(includes([1, 2, 3], 1))           # True
print(includes([1, 2, 3], 1, 2))        # False; starting from index 2, search for the value of 1
print(includes({'a': 1, 'b': 2}, 1))    # True
print(includes({'a': 1, 'b': 2}, 'a'))  # False; search for the value of 'a', NOT key of 'a'
print(includes('abcd', 'b'))            # True
print(includes('abcd', 'e'))            # False; value of 'e' is non-existent in the collection
