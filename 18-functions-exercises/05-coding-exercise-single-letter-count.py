# Write a function called single_letter_count
# Takes two parameters (a word & a letter, respectively)
# Returns the number of times (integer) the letter appeared in the word
# Function should use case-insensitive
# If the letter is not found in the word, return 0

def single_letter_count(word, letter):
    "single_letter_count(word, letter) returns the number of times the letter appeared in the word."
    return word.lower().count(letter.lower())


print("Function: single_letter_count()")
print(f"Documentation: {single_letter_count.__doc__}")
user_input_word = str(input("Enter word: "))
user_input_letter = str(input("Enter letter: "))
print(f"The letter {user_input_letter} appeared {single_letter_count(user_input_word, user_input_letter)} times.")
