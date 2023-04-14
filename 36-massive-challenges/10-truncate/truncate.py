# Write a function called truncate()
# It accepts both string and an integer argument values
# The integer value dictates the length of the new string to be returned based on the passed string value
# The truncated string MUST include a suffix of '...' as part of the returned string length
# string_length less than 3 returns a message 'Truncation must be at least 3 characters'
# string_length == 3 returns the string '...'
# string_length greater than the string value returns the same string


def truncate(string_data, string_length):
    """truncate(str, int) returns a new string based on the passed integer value."""
    print(f"string length: {len(string_data)}")
    if string_length < 3:
        return "Truncation must be at least characters."
    elif string_length == 3:
        return "..."
    elif string_length >= len(string_data):
        return string_data
    # The '-3' in range() is to accommodate the '...' suffix
    return "".join([string_data[letter] for letter in range(string_length - 3)]) + "..."


# Test Code
print(truncate("Super cool", 2))
print(truncate("Super cool", 1))
print(truncate("Super cool", 10))
print(truncate("Hello World", 6))
print(truncate("Problem solving is the best!", 10))
print(truncate("Another test", 12))
print(truncate("Woah", 4))
print(truncate("Woah", 3))
print(truncate("Yo!", 100))
print(truncate("Holy Guacamole!", 152))
