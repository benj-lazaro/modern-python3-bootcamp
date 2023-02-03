# Write a function called capitalize
# Accepts 1 parameter (string)
# Returns the same string with the 1st letter in uppercase

def capitalize(string_data):
    """capitalize(string) returns the string with the 1st letter in uppercase."""
    return string_data[0].upper() + string_data[1:]


print("Function: capitalize()")
print(f"Documentation: {capitalize.__doc__}")
user_input = str(input("Enter a string in lowercase: "))
print(f"Result: {capitalize(user_input)}")
