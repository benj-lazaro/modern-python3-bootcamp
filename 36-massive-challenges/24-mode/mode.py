# Write a function called mode()
# It accepts a list of integers
# Returns the most frequent integer in the list


def mode(number_list):
    """mode(list) returns the most frequent number in the list."""
    high_frequency_count = 0
    frequent_integer = ""

    for index in range(len(number_list)):
        frequency_count = number_list.count(number_list[index])
        if frequency_count > high_frequency_count:
            high_frequency_count = frequency_count
            frequent_integer = number_list[index]

    return frequent_integer


# Test Code
print(mode([2, 4, 1, 2, 3, 3, 4, 4, 5, 4, 4, 6, 4, 6, 7, 4]))
print(mode([2, 2, 1, 1, 0, 0, 0, 0, 0, 0, 0, 4, 2]))
print(mode([9, 9, 0, 1, 2, 3, 4, 5, 8, 8, 8, 8, 8, 8, 8, 100]))
