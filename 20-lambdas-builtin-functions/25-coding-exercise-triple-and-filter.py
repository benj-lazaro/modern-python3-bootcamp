# Write a function called triple_and_filter
# Accepts a list of numbers
# Filter out every item NOT divisible by 4
# Return a new list with every number divisible by 4 tripled

def triple_and_filter(list_number):
    """triple_and_filter(list) returns a list with every number divisible by 4 tripled."""
    return [number * 3 for number in list_number if number % 4 == 0]


print("Function: triple_and_filter()")
print(f"Documentation: {triple_and_filter.__doc__}")

list_data = [1, 2, 3, 4]
print(f"\nlist_data: {list_data}")
print(f"Statement: triple_and_filter(list_data)")
print(f"Result: {triple_and_filter(list_data)}")

list_data = [6, 8, 10, 12]
print(f"\nlist_data: {list_data}")
print(f"Statement: triple_and_filter(list_data)")
print(f"Result: {triple_and_filter(list_data)}")
