# Dictionary comprehension syntax
# {<key>:<value> for <key, value or variable> in <iterable_object>}

numbers = {
    "first": 1,
    "second": 2,
    "third": 3
}
print(numbers)

print("\nCreate a new dictionary containing squared values of the dictionary numbers")
result = {key: value ** 2 for key,value in numbers.items()}
print(f"numbers: {numbers}")
print(f"Result: {result}")

print("\nCreate a new dictionary containing squared values of the list [1, 2, 3, ,4 ,5, 6]")
result = {num: num ** 2 for num in [1, 2, 3, 4, 5, 6]}
print(f"Result: {result}")

print("\nCreate a new dictionary containing the combination of string1 as key and string2 as value")
string1 = "ABC"
string2 = "123"
print(f"string1: {string1}")
print(f"string2: {string2}")
result = {string1[index]: string2[index] for index in range(0, len(string1))}
print(f"Result: {result}")

print("\nCreate a new dictionary containing uppercased items of dictionary instructor")
instructor = {
    "name": "Colt Steele",
    "city": "San Francisco",
    "color": "purple"
}
print(f"instructor: {instructor}")
result = {key.upper(): value.upper() for key,value in instructor.items()}
print(f"Result: {result}")

print("\nCreate a new dictionary with the key 'color' of dictionary instructor uppercased")
instructor = {
    "name": "Colt Steele",
    "city": "San Francisco",
    "color": "purple"
}
print(f"instructor: {instructor}")
result = {(key.upper() if key == 'color' else key): value.upper() for key, value in instructor.items()}
print(result)


# Dictionary comprehension with conditional logic
print("\nCreate a new dictionary containing items whose value if categorized as either even or odd number"
      " taken from a list")
number_list = [1, 2, 3, 4]
print(f"number: {number_list}")
result = {number: ("even" if number % 2 == 0 else "odd") for number in number_list}
print(f"Result: {result}")

print("\nCreate a new dictionary containing items whose value if categorized as either even or odd number"
      " taken from range 1 to 100")
result = {number: ("even" if number % 2 == 0 else "odd") for number in range(1, 101)}
print(f"Result: {result}")
