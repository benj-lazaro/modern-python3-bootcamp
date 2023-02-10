# Write a function called extract_full_name
# Accepts a list of dictionaries items
# Returns a list of string with the first and last name key values from each dictionary concatenated

def extract_full_name(dict_data):
    """extract_full_name(dict) returns a list with the first & last names from each dictionary concatenated"""
    first_name = list(map(lambda name: name['first'], dict_data))
    last_name = list(map(lambda name: name['last'], dict_data))
    return [''.join(' '.join(string)) for string in zip(first_name, last_name)]

    # Colt Steele's solution
    # return list(map(lambda name: "{} {}".format(name['first'], name['last']), dict_data))

name_list = [{'first': 'Elie', 'last': 'Schoppik'}, {'first': 'Colt', 'last': 'Steele'}]
print("Function: extract_full_name()")
print(f"Documentation: {extract_full_name.__doc__}")
print(f"\nname_list: {name_list}")
print("Statement: extract_full_name(name_list)")
print(f"Result: {extract_full_name(name_list)}")
