# Combining filter() and map()

# Return a new list with the string "Your instructor is " with each value in the given list
# Applicable ONLY to names with less than 5 characters
name_list = ["Lassie", "Colt", "Rusty"]

# My solution
filter_names = list(filter(lambda name: len(name) < 5, name_list))
map_names = list(map(lambda name: print(f"Successive map & filter: Your instructor is {name}"), filter_names))

# Instructor solution
solution = list(map(lambda name: f"Your instructor is {name}.", filter(lambda name: len(name) < 5, name_list)))
print(f"single-line map & filter combo: {solution}")

# List comprehension
list_comprehension = [f"Your instructor is {name}" for name in name_list if len(name) < 5]
print(f"List comprehension: {list_comprehension}")
