# Write a function called is_valid_time()
# Accepts a single string argument
# Returns True if string is formatted correctly as a time (e.g. 3:15 or 12:48)
# Otherwise, returns False
# NOTE: time can start with a single number or two

import re


def is_valid_time(string_input):
    """is_valid_time(str) returns True if passed string is formatted correctly as time."""
    time_regex = re.compile(r"\b\d\d?:\d{2}\b")
    match = time_regex.fullmatch(string_input)

    if match:
        return True
    return  False


# Test Code
print("Testing is_valid_time()...")
print(is_valid_time("10:45"))   # True
print(is_valid_time("1:23"))    # True
print(is_valid_time("10.45"))   # False
print(is_valid_time("1999"))    # False
print(is_valid_time("145:23"))  # False
