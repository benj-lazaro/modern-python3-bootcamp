# Write a function called is_palindrome()
# Accepts 1 parameter (string)
# Check if it is a palindrome
# Return True if it is otherwise False

def is_palindrome(string_data):
    """is_palindrome(string) checks if the string is a palindrome. If it is returns True, otherwise False."""
    reverse_string = string_data[::-1]
    if string_data == reverse_string:
        return True
    return False

print("Function: is_palindrome()")
print(f"Dcumentation: {is_palindrome.__doc__}")
user_string = str(input("Enter a string: "))
print(f"Is the string '{user_string}' a palindrome: {is_palindrome(user_string)}")
