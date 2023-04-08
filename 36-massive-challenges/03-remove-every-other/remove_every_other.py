# Write a function called remove_every_other
# It accepts a list
# Returns a new list with every second item removed

def remove_every_other(user_list):
    """remove_every_other(list) returns a new list with every 2nd item removed."""
    return user_list[::2]


# Test Code
print(remove_every_other([1, 2, 3, 4, 5]))
print(remove_every_other([5, 1, 2, 4, 1]))
print(remove_every_other([1]))
