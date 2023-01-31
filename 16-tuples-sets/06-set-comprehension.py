# Set Comprehension

# Set of squared numbers from 0 to exclusive 10
print("Set of squared numbers from 0 to (exclusive) 10:")
result = {number ** 2 for number in range(10)}
print(f"Result: {result}")

# Dictionary of squared numbers from 0 to exclusive 10
print("\nDictionary of squared numbers from 0 to (exclusive) 10:")
result = {number: number ** 2 for number in range(10)}
print(f"Result: {result}")

# Set of uppercase characters from a string
print("\nSet of uppercase characters from a string")
result = {character.upper() for character in 'Hello'}
print(f"Result: {result}")

# Function that accepts a string and return True if the string contains all of the vowels else False
def are_all_vowels_in_string(string):
    return len({character for character in string if character in 'aeiou'}) == 5

print("\nReturns True if the passed string contains all of the vowels else False:")
string_value = "sequoia"
print(f"string_value: {string_value}")
result = are_all_vowels_in_string(string_value)
print(result)
