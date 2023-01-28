# Dictionary methods: .clear(), .copy()

# .clear() = clears all keys & values in a dictionary
print("\n.clear() method")
sample_dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(f"Dictionary content: {sample_dictionary}")
sample_dictionary.clear()
print(f"Post-operation Dictionary content: {sample_dictionary}")


# .copy() = makes a copy of a dictionary
print("\n.copy() method")
original_dictionary = {
    "a": 1,
    "b": 2,
    "c": 3
}
print(f"Original dictionary: {original_dictionary}")
duplicate_dictionary = original_dictionary.copy()
print(f"Duplicate dictionary: {duplicate_dictionary}")

# Check if original & duplicate dictionaries references to the same memory; returns False if it is a copy
print(f"Duplicate & Original dictionary located on the same memory: {duplicate_dictionary is original_dictionary}")


# .fromkeys() = creates key-value pairs from comma-separated values; used to generate default values to keys
print("\n.fromkeys() method")
sample_dictionary = {}.fromkeys("a", 1)
sample_dictionary = {}.fromkeys("b", 2) # Overwrites previous dictionary content
sample_dictionary = {}.fromkeys("c", 3) # Overwrites previous dictionary content
print(sample_dictionary)

new_user = {}.fromkeys(["name", "score", "email", "profile_bio"], "unknown")
print(new_user)


# .get() = Retrieves the value of a key in an object & return None if the key is non-existent
print("\n.get() method")
sample_dictionary = {
    "a": 1,
    "b": 2,
    "c": 3,
    "power": 4
}
result = sample_dictionary.get("c")
print(result)

result = sample_dictionary.get("d")
print(result)

result = sample_dictionary.get("power")
print(result)
