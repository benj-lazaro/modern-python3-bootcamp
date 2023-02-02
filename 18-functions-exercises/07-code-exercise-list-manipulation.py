# Write a function called list_manipulation
# Accepts founr parameters (a list, a command, a location & a value)
# command = add, remove
# location = beginning, end
# Returns the list with updated items

def list_manipulation(list_data, command, location, value=None):
    """list_manipulation(list, cmd=add/remove, location=beginning/end, value) accepts 4 parameters; returns removed item or updated list."""

    if command == "add":
        if location == "beginning":
            list_data.insert(0, value)
            return f"{command} item {value} at the {location} of the list: {list_data}"
        list_data.append(value)
        return f"{command} item {value} at the {location} of list: {list_data}"
    else:
        if location == "beginning":
            return f"{command} item {list_data.pop(0)} at the {location} of the list: {list_data}"
        return f"{command} item {list_data.pop()} at the {location} of the list: {list_data}"

list_sample = [1, 2, 3, 4, 5]
print("Function: list_manipulation()")
print(f"Documentation: {list_manipulation.__doc__}")

print(f"\nStarting list content: {list_sample}")
print(list_manipulation(list_sample, "add", "beginning", 0))
print(list_manipulation(list_sample, "add", "end", 7))
print(list_manipulation(list_sample, "remove", "beginning"))
print(list_manipulation(list_sample, "remove", "end"))
