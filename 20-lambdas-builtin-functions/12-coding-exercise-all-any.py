# Write a function called is_all_strings
# Accepts a single parameter
# Returns True if it ONLY (ALL) contains strings else False

def is_all_strings(data):
    """is_all_strings(data) return True if argument value(s) is/are a string."""
    return all([type(value) == str for value in data])

print("Function: is_all_strings()")
print(f"Documentation: {is_all_strings.__doc__}")
print("Statement: is_all_strings([1, 2, 4])")
print(f"Result: {is_all_strings([1, 2, 4])}")

print("\nStatement: is_all_strings(['a', 'b', 'c'])")
print(f"Result: {is_all_strings(['a', 'b', 'c'])}")

print("\nStatement: is_all_strings([1, 'strong', 0.34234])")
print(f"Result: {is_all_strings([1, 'strong', 0.34234])}")

print("\nStatement: is_all_strings(['far', 'from', 'weak'])")
print(f"Result: {is_all_strings(['far', 'from', 'weak'])}")
