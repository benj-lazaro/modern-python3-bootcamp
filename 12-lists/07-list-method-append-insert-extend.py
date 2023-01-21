# List methods append, insert & extend

# .append() method = adds 1 item to the end of a list
print("Using .append() method")
first_list = [1, 2, 3, 4]
print(first_list)

first_list.append(5)
print(first_list)

# .extend() method = adds more than 1 item individually to the end of a list
print("\nUsing .extend() method")
second_list = [1, 2, 3, 4]
print(second_list)

second_list.extend([5, 6, 7, 8])
print(second_list)

# .insert() method = inserts an item at a given position in a list
print("\nUsing .insert() method")
third_list = [1, 2, 3, 4]
print(third_list)

third_list.insert(2, "Hey there")
print(third_list)

# Does not work due to insert() uses the old index value before updating the list & inserting new item
third_list.insert(-1, "Supposed Last item")
print(third_list)

# To address previous issue, use len() to determine length of list to identify index of last item
# Before inserting the item into the list
third_list.insert(len(third_list), "Real Last item")
print(third_list)
