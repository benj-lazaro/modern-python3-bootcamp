# Given two lists
list1 = ["CA", "NJ", "RI"]
list2 = ["California", "New Jersey", "Rhode Island"]

# Create a dictionary with list1 items as key and list2 items as value
# Save dictionary to a variable called result
result = {list1[index]: list2[index] for index in range(0, len(list1))}
print(f"Result: {result}")
