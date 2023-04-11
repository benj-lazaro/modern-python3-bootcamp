# Write a function called titleize()
# Accepts a string of words
# Returns a new string with the 1st letter of every word capitalized


def titleize(word_input):
    """titleize(str) returns a new string with the 1st letter of every word capitalized."""
    return " ".join(word[0].upper() + word[1::].lower() for word in word_input.split())


# Test Code
print(titleize("this is awesome"))
print(titleize("oNLy cAPITALIZE fIRSt lETTER oF eVERT wORD"))
print(titleize("ALL CAPS LETTERS IN A WORD."))
