# Dictionary methods: .pop(), .popitems(), .update()

# .pop() = accepts a key, removes the corresponding key-value pair (item) & returned popped value
print(".pop() method")
dictionary_sample = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(f"dictionary_sample: {dictionary_sample}")
popped_value = dictionary_sample.pop("b")
print(f"post-operation check: {dictionary_sample}")
print(f"Popped value: {popped_value}")


# .popitem() = removes the key-value pair (item) that was last inserted into the dictionary
print("\n.popitem() method")
dictionary_sample = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5
}
print(f"dictionary_sample: {dictionary_sample}")
popped_item = dictionary_sample.popitem()
print(f"post-operation check: {dictionary_sample}")
print(f"Popped item: {popped_item}")


# .update() = updates keys & values in a dictionary with another set of key-value pairs
print("\n.update() method")
first_dictionary = {
    "a": 1,
    "b": 2,
    "c": 3,
    "d": 4,
    "e": 5
}

second_dictionary = {}
print(f"first_dictionary: {first_dictionary}")
print(f"second_dictionary: {second_dictionary}")

print("\nUpdate content of second_dictionary with first_dictionary's items using .update()")
second_dictionary.update(first_dictionary)
print(f"first_dictionary: {first_dictionary}")
print(f"second_dictionary: {second_dictionary}")

print("\nAssign a new value to the second_dictionary's key 'a':")
second_dictionary["a"] = "amazing"
print(f"first_dictionary: {first_dictionary}")
print(f"second_dictionary: {second_dictionary}")

print("\nOverride content of second_dictionary with first_dictionary's items using .update()")
second_dictionary.update(first_dictionary)
print(f"first_dictionary: {first_dictionary}")
print(f"second_dictionary: {second_dictionary}")
