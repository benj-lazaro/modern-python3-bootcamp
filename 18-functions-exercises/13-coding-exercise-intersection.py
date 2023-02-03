# write a function called intersection
# Accepts two parameters (lists)
# Returns a list with values existing in both lists

def intersection(list_one, list_two):
    """intersection(list1, list2) returns a list with values existing in both lists."""
    return [item for item in list_one if item in list_two]


list_one_data = [1,2,3]
list_two_data = [2,3,4]
print("Function: intersection()")
print(f"Documentation: {intersection.__doc__}")
print(f"list_one: {list_one_data}")
print(f"list_two: {list_two_data}")
print(f"Result: {intersection(list_one_data, list_two_data)}")
