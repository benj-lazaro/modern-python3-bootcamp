# Write a function called min_max_key_in_dictionary()
# It accepts a dictionary
# Returns a list with the lowest and highest key in the passed dictionary
# Dictionary keys are integers

def min_max_key_in_dictionary(dict_data):
    """min_max_key_in_dictionary(dict) returns a list with the lowest & highest integer dictionary key."""
    sort_keys = sorted(dict_data.keys())
    return [sort_keys[0], sort_keys[-1]]


# Test Code
print(min_max_key_in_dictionary({2: 'a', 7: 'b', 1: 'c', 10: 'd', 4: 'e'}))
print(min_max_key_in_dictionary({1: "Elie", 4: "Matt", 2: "Tim"}))
