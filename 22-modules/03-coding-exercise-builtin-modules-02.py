from keyword import iskeyword
# Write a function called contains_keyword
# Accepts any number of strings arguments
# Returns True if the argument value is a valig Python keyword; otherwise False
# Import the module keyword and use the built-in function iskeyword()

def contains_keyword(*args):
    """contains_keyword(*args) return True if any of the arguments contains a valid keyword; otherwise False."""
    for item in args:
        if iskeyword(item):
            return True
    return False


print("FunctionL contains_keyword()")
print(f"Documentation: {contains_keyword.__doc__}")
print("\nStatement: contains_keyword('hello', 'goodbye')")
print(f"Result: {contains_keyword('hello', 'goodbye')}")

print("\nStatement: contains_keyword('def', 'haha', 'lol', 'chicken', 'alaska')")
print(f"Result: {contains_keyword('def', 'haha', 'lol', 'chicken', 'alaska')}")

print("\nStatement: contains_keyword('four', 'for', 'if')")
print(f"Result: {contains_keyword('four', 'for', 'if')}")

print("\nStatement: contains_keyword('blah', 'doggo', 'crab', 'anchor')")
print(f"Result: {contains_keyword('blah', 'doggo', 'crab', 'anchor')}")

print("\nStatement: contains_keyword('grizzly', 'ignore', 'return', 'False') ")
print(f"Result: {contains_keyword('grizzly', 'ignore', 'return', 'False')}")

