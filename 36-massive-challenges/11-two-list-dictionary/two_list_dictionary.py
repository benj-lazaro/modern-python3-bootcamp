# Write a function called two_list_dictionary()
# It accepts two lists of varying lengths
# The 1st list consists of keys
# The 2nd list consists of values
# Returns a dictionary created from the keys and values
# If there are NOT enough values, the remaining keys should have the value of null


def two_list_dictionary(list_keys, list_values):
    """two_list_dictionary(list, list) returns a new dictionary using the passed lists as content."""
    if len(list_keys) != len(list_values):
        temp_list = []
        dictionary = {}

        try:
            for item in range(len(list_keys)):
                temp_list.append(list_values[item])
                dictionary = dict(zip(list_keys, temp_list))
        except IndexError:
            temp_list.append("None")
            dictionary = dict(zip(list_keys, temp_list))
        return dictionary

    return dict(zip(list_keys, list_values))


# Test Code
print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3, 4]))
print(two_list_dictionary(['a', 'b', 'c', 'd'], [1, 2, 3]))
print(two_list_dictionary(['x', 'y', 'z'], [1, 2]))
