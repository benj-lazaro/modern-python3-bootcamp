# Iterating dictionary key-values pairs
instructor = {
    "name": "Colt",
    "owns_dog": True,
    "number_of_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my_favorite_number!"
}

# Iterate through dictionary values using for loop & .values()
print("\nIterate and print dictionary values using .values():")
for value in instructor.values():
    print(value)

# Iterate through dictionary keys using for loop & .keys()
print("\nIterate and print dictionary keys using .keys():")
for key in instructor.keys():
    print(key)

# Iterate through dictionary keys & values using for loop & .items() -> returns a tuple
print("\nIterate and print both dictionary keys and values using .items()")
for key,value in instructor.items():
    print(f"Key is {key} & Value is {value}")
