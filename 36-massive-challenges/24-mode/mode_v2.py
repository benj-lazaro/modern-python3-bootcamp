# Version 02
def mode(number_list):
    """mode(list) returns the most frequent number in the list."""
    instance_count = {value: number_list.count(value) for value in range(len(number_list))}
    frequent_integer = max(instance_count.values())
    frequent_item = list(instance_count.values()).index(frequent_integer)
    return frequent_item


# Test Code
print(mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4]))
print(mode([2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 4, 2]))
print(mode([9, 9, 0, 1, 2, 3, 4, 5, 8, 8, 8, 8, 8, 8, 8, 100]))
