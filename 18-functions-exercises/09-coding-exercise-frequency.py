# Write a function called frequency
# Accepts a two parameters (list, search_term)
# Returns the number of times the search_term appeared in the list

def frequency(list_data, search_item):
    """frequency(list, search_item) returns the number of times the search_item appeared in the list."""
    return list_data.count(search_item)


fruit_list = ["apple", "banana", "cherry", "guava", "kiwi", "lemon", "lime", "orange", "apple", "banana"]
print("Function: frquency()")
print(f"Documentation: {frequency.__doc__}")
print(f"fruit_list: {fruit_list}")
print(f"The search item 'apple' appeared {frequency(fruit_list, 'apple')} time(s).")
print(f"The search item 'banana' appeared {frequency(fruit_list, 'banana')} time(s).")
print(f"The search item 'lime' appeared {frequency(fruit_list, 'lime')} time(s).")
