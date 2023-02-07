# map = a standard function that accepts (at least) two arguments:
# * a function (usually a lambda) that works with each item of an iterable
# * an iterable (list, string, dictionary, tuple, set)
# Returns a map object w/c can be converted into another data structure
# NOTE: map object is iterated once

even_number_list = [2, 4, 6, 8, 10]
print(f"Iterable even_number_list: {even_number_list}")

# Iterate through each list item, double its value & save into a map object
doubles = map(lambda number: number * 2, even_number_list)
# Converts map object doubles into a list
print(f"map object doubles: {list(doubles)}")
print(f"map object doubles: {list(doubles)}")   # demo that a map object is iterated once

name_list = ["Darcy", "Christina", "Dana", "Annabel"]
print(f"\nIterable name_list: {name_list}")
# Iterable through each list item, uppercase its value & save into a map object
peeps = map(lambda name: name.upper(), name_list)
print(f"map object peeps: {list(peeps)}")

name_dict_list = [
    {"first": "Rusty", "last": "Steele"},
    {"first": "Colt", "last": "Steele"},
    {"first": "Blue", "last": "Steele"}
]

print(f"\nIterable name_dict_list: {name_dict_list}")
first_name = map(lambda name: name["first"], name_dict_list)
print(f"map object first_name: {list(first_name)}")
