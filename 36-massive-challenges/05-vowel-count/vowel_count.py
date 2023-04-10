# Write a function call vowel_count()
# It accepts a string
# Returns a dictionary with keys as the vowels & values as the count of times that vowels appeared in the string

def vowel_count(user_string):
    """vowel_count(str) return a dictionary containing the count of times a vowel appeared in the string."""
    string_input = user_string.lower()
    return {letter: string_input.count(letter) for letter in string_input if letter in "aeiou"}


# Test Code
print(vowel_count('awesome'))
print(vowel_count('Elie'))
print(vowel_count('Colt'))
