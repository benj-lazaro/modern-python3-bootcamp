# Using in with dictionaries
instructor = {
    "name": "Colt",
    "owns_dog": True,
    "number_of_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my_favorite_number!"
}

# Test for the existence of a key in a dictionary
result = "name" in instructor
print(f"Is the key 'name' exists in dictionary instructor: {result}")

result = "address" in instructor
print(f"Is the key 'address' exists in dictionary instructor: {result}")


# Test for the existence of a value in a dictionary
result = "Colt" in instructor.values()
print(f"\nIs the value 'Colt' exists in dictionary instructor: {result}")

result = "Nope!" in instructor.values()
print(f"Is the value 'Nope!' exists in dictionary instructor: {result}")
