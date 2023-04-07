# Write a function called reverse_string()
# Accepts a string
# Returns a new string with all the characters reverse

def reverse_string(user_string):
    """reverse_string(str) accepts a string and a new string with all characters in reverse."""
    return user_string[::-1]


# Test Code
user_input = str(input("Please enter a string: "))
returned_value = reverse_string(user_input)
print(f"Reverse string: {returned_value}")
