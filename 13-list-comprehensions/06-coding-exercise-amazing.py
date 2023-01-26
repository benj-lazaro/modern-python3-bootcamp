# Given a string "amazing"
# Create a variable called answer
# Assign all letters of the string that are NOT vowels (a, e, i, o and u)
answer = [letter for letter in "amazing" if letter not in "aeiou"]
print(f"answer: {answer}")
