# Accessing data in dictionaries
instructor = {
    "name": "Colt",
    "owns_dog": True,
    "number_of_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my_favorite_number!"
}

cat = dict(name="kitty", age=0.5)

# Access & print dictionary value using dictionary key
print(instructor["name"])
print(instructor[44])

print(cat["name"])
print(cat["age"])
