# List methods clear, pop & remove

# .clear() method = removes all items from a list at once
print("Using .clear() method")
number_list = [1, 2, 3, 4]
print(number_list)

number_list.clear()
print(number_list)

# .pop() method = removes an item at a given position in the list (or last item by default) & returns it
print("\nUsing .pop() method")
number_list = [1, 2, 3, 4]
print(number_list)

removed_item = number_list.pop(2)
print(f"Popped item: {removed_item}")
print(number_list)

removed_item = number_list.pop()
print(f"Popped item: {removed_item}")
print(number_list)

# .remove() method = removes the 1st instance of an item by value (not by index) in a list & does NOT return it
# Throws a ValueError if item is NOT found
print("\nUsing .remove() method")
number_list = [1, 2, 3, 4, 4, 5]
print(number_list)

number_list.remove(4)
print(number_list)
