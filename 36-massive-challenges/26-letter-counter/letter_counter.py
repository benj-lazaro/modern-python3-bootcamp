# Write a function called letter_counter()
# It accepts a string and returns a function
# The inner function accepts a parameter of a (forced) lowercase alphanet character
# It returns the number of times the character appeared in the string


def letter_counter(string_value):
    """letter_counter(str) returns the number of times the searched character appears in the passed string."""
    def inner_function(character_value):
        nonlocal string_value

        print(f"Passed String: {string_value}")
        print(f"Character Search: {character_value}")
        return string_value.lower().count(character_value)
    return inner_function


# Test Code
character_count = letter_counter("Amazing")
print(f"Character Count: {character_count('a')}\n")
print(f"Character Count: {character_count('m')}\n")

character_count = letter_counter("This Is Really Fun!")
print(f"Character Count: {character_count('i')}\n")
print(f"Character Count: {character_count('l')}\n")
print(f"Character Count: {character_count('!')}\n")