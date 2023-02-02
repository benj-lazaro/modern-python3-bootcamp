# Write a function called last_element
# Takes 1 parameter (a list)
# Returns the last value in the list
# It should return None if the list is empty

def last_element(list_data):
    """last_element(list) accepts a list and returns the last item; returns None if the list is empty."""
    if len(list_data) == 0:
        return None
    return list_data.pop()


user_list = ["Andrea", "Jessica", "Mica", "Mirai", "Azumi"]
number_list =[123, 232, 343, 234]
empty_list = []

print("Function: last_element()")
print(f"Documentation: {last_element.__doc__}")
print(f"Last element of user_list: {last_element(user_list)}")
print(f"last element of number_list: {last_element(number_list)}")
print(f"Last element of empty_list: {last_element(empty_list)}")
