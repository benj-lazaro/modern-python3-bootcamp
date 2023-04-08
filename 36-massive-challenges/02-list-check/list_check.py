# Write a function called list_check
# It accepts a list
# Returns True if each item is a list type
# Otherwise, returns False

def list_check(user_list):
    """list_check(list) return True if every item in the list is a list type; otherwise returns False."""
    for item in user_list:
        if type(item) is not list:
            return False
    return True


# Test Code
print(list_check([[], [1], [2, 3], (1, 2)]))
print(list_check([1, True, [], [1], [2, 3]]))
print(list_check([[], [1], [2, 3]]))
