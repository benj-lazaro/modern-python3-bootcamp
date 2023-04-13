# Write a function called repeat()
# It accepts a string and a number
# Returns a new string with the passed string repeated the number amount of times
# DO NOT use the built-in .repeat() method


def repeat(user_string, repeat_count):
    """repeat(str, int) returns a new string repeated a number of times."""
    return user_string * repeat_count


print(repeat('*', 3))       # Returns the new string with '*' repeated 3 times
print(repeat('*', 100))     # Returns the new string with '*' repeated a 100 times
print(repeat('abc', 2))     # Returns the new string with 'abc' repeated twice
print(repeat('abc', 0))     # Returns an empty line

