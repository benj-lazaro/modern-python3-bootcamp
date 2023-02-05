# Write a function called combine_words
# Accepts a single string called word and any number of additional keyword arguments
# If a 'prefix' is provided, return the prefix followed by the word
# If a 'suffix' is provided, return the word followed by the suffix
# If neither (prefix/suffix) is provided, return the word

def combine_words(string_word, **kwargs):
    """combine_word(string, **kwargs) returns a passed string or combination of positional string values."""
    if "prefix" in kwargs.keys():
        return f"{kwargs['prefix']}" + string_word
    elif "suffix" in kwargs.keys():
        return string_word + f"{kwargs['suffix']}"
    else:
        return string_word


print("Function: combine_words()")
print(f"Documentation: {combine_words.__doc__}")
print(combine_words("hack", prefix="gibson "))
print(combine_words("hack", suffix=" the planet!"))
print(combine_words("hack", suffix="er"))
