# Write a function called multiple_letter_count
# Takes one parameter (a string)
# Returns a dictionary with the letters being the keys & values being the count of letters

def multiple_letter_count(string_data):
    """multiple_letter_count(string) accepts a word and returns a dictionary with letters as keys & number of occurences (within the word) as value"""
    return {letter: string_data.count(letter) for letter in string_data}

print("Function: multiple_letter_count()")
print(f"Documentation: {multiple_letter_count.__doc__}")
user_input_word = str(input("Enter word: "))
print(f"Result: {multiple_letter_count(user_input_word)}")
