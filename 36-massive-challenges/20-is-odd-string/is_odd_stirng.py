# Write a function is_odd_string()
# It accepts a single word string
# Returns True if the sum of each character in the alphabet is odd
# Otherwise, returns False


def is_odd_string(string_data):
    """is_odd_string(str) returns True if the alphabet value sum of each character in the string is odd."""
    index_sum = sum((ord(character) - 96) for character in string_data.lower()) or 0
    return index_sum % 2 == 1


# Test Code
print(is_odd_string('a'))           # Returns True
print(is_odd_string('aaaa'))        # Returns False
print(is_odd_string('amazing'))     # Returns True
print(is_odd_string('veryfun'))     # Returns True
print(is_odd_string('veryfunny'))   # Returns False
print(is_odd_string('AAAA'))        # Returns False
print(is_odd_string('TESLA'))       # Returns True
