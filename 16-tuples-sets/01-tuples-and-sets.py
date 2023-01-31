# Basic syntax of a tuple
# (<value_1>, <value_2>, <value_n>)    = immutable data structure

# Attempting to add/delete/modify a value in a tuple will trigger a TypeError
# Tuples are FASTER than Lists

# Accessing tuple values
print("Accessing tuple items")
alphabet_tuple = ("a", "b", "c", "d", "e")
print(alphabet_tuple)

month_tuple = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October",
               "November", "December")
print(month_tuple)
print(month_tuple[0])
print(month_tuple[-1])

# Tuple as keys in a dictionary; a List can NOT be used as a dictionary key
print("\nTuple as keys in a dictionary")
location = {
    (33.4005, 39.0817): "Tokyo office",
    (40.7128, 74.0060): "New York office",
    (37.7749, 122.4198): "San Francisco office"
}
print(location)

print("\nAccessing 1st item dictionary")
print(location[(33.4005, 39.0817)])

# Dictionary method .items(), returns a Tuple items
print("\nDictionary method .items() returns a list of tuple items ")
cat = {
    "name": "Biscuit",
    "age": 0.5,
    "favorite_toy": "my chapstick"
}
result = cat.items()
print(f"Dictionary: {cat}")
print(f"Result: {result}")


