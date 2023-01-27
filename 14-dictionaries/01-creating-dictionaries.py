# Basic syntax of a dictionary
instructor = {
    "name": "Colt",
    "owns_dog": True,
    "num_courses": 4,
    "favorite_language": "Python",
    "is_hilarious": False,
    44: "my favorite number!"
}
print(instructor)

cat = {
    "name": "Blue",
    "age": 3.5,
    "isCute": True
}
print(cat)

# Dictionary as a list item
shopping_cart = [{
    "name": "cat litter",
    "quantity": 3,

}]
print(shopping_cart)


# Another way to create a dictionary using dict()
cat2 = dict(
    name="kitten",
    age=0.5,
    isCute=True
)
print(cat2)
