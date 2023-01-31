# 1 - Create a variable called numbers which is a tuple with the the values 1, 2, 3 and 4 inside.
numbers = (1, 2, 3, 4)
print(f"numbers: {numbers}")

# 2 - Create a variable called value which is a tuple with the the value 1 inside.
value = (1,)
print(f"value: {value}")

# 3 - Given the following variable:
values = [10,20,30]
print(f"values: {values}")

# Create a variable called static_values which is the result of the values variable converted to a tuple
static_values = tuple(values)
print(f"static_values: {static_values}")

# 4 - Given the following variable
stuff = [1, 3, 1, 5, 2, 5, 1, 2, 5]
print(f"stuff:{stuff}")

# Create a variable called unique_stuff which is a set of only the unique values in the stuff list
unique_stuff = set(stuff)
print(f"unique_stuff: {unique_stuff}")
