# Write a function called valid_parenthesis
# It accepts a string of parenthesis
# Checks if the order of parenthesis is valid
# Returns True if the order is correct
# Otherwise return False


def valid_parentheses(string_data):
    """valid_parenthesis(str) returns True if the parenthesis order is correct, otherwise False."""
    # Check if the pair of ( and ) are equal
    if string_data.count("(") == string_data.count(")"):
        # Check order of parenthesis pairing is correct
        for index in range(len(string_data)):
            # Check if '(' is less than ')' which means the order is invalid
            if string_data[:index].count('(') < string_data[:index].count(')'):
                return False
        return True
    return False


# Test Code
print(valid_parentheses("()"))              # Returns True
print(valid_parentheses(")(()))"))          # Returns False
print(valid_parentheses("("))               # Returns False
print(valid_parentheses("(())((()())())"))  # Returns True
print(valid_parentheses('))(('))            # Returns False
print(valid_parentheses('(())'))            # Returns True
