# Write a function called contains_purple
# Accepts any number of arguments
# Returns True if any of the arguments has "purple"
# Otherwise, returns False

def contains_purple(*args):
    """contains_purple(*args) accepts any number of arguments; returns True if it contains 'purple' else False."""
    if "purple" in args:
        return True
    return False

print("Function: contains_purple()")
print(f"Documentation: {contains_purple.__doc__}")
print("Test data: 'blue', 1, True, False, 'green', 'fushia', 12345")
print(f"Result: {contains_purple('blue', 1, True, False, 'green', 'fushia', 12345)}")

print("\nTest data: 'pink', 1, 456656, 'purple', 'black', True, True")
print(f"Result: {contains_purple('pink', 1, 456656, 'purple', 'black', True, True)}")
