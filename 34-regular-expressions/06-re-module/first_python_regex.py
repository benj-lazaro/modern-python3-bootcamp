# First regex program in Python
import re

test_string1 = "123456789 this is a test string with no phone number"
test_string2 = "Call me at 123 456-7890 or 890 765-4321"

# Pass the regex pattern as a raw string to .compile() method
# Raw string prevents the need to include an escape character \ for \ in the regex pattern
# .compiler() returns a regex object & stored into the variable phone_number_pattern
phone_number_pattern = re.compile(r"\d{3} \d{3}-\d{4}")

# .search() scan through the passed string and returns the 1st matching instance as a match object
# Returns None when no matching text is found
result = phone_number_pattern.search(test_string1)
print(result)

result = phone_number_pattern.search(test_string2)
print(result)

# Use .group() to extract the corresponding value from the returned match object
# Raises an AttributeError if the returned match object = None
matching_text = result.group()
print(matching_text)

# User .findall() to scan the passed string and returns all matching instances as a list of strings
result = phone_number_pattern.findall(test_string2)
print(result)
print(result[0])
print(result[1])
