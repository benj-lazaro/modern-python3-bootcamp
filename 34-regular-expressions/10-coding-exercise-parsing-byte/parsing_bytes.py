# Write a function called parse_bytes()
# Accepts a single string
# Returns a list of binary bytes contained in the string
# Each byte is a combination of eight 0s and 1s

import re


def parse_bytes(string_input):
    """parse_bytes(str) returns a list of a byte (base2 format) embedded in a string."""
    byte_regex = re.compile(r"\b[01]{8}\b")
    match = byte_regex.findall(string_input)

    if match:
        return match
    return None


# Test Code
print(parse_bytes("11010101 101 323"))  # ['11010101']
print(parse_bytes("my data is: 10101010 11100010"))  # ['10101010', '11100010']
print(parse_bytes("This is a test."))  # []
