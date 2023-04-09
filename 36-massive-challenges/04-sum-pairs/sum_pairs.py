# Write a function called sum_pairs
# It accepts a list (containing integers) and a separate integer
# Returns a pair of integers from the list that when summed is equivalent to the passed integer


def sum_pairs(user_list, user_number):
    """sum_pairs(list, int) returns the pair of items that is equivalent to the passed integer value."""
    number_pair = []

    for index in range(len(user_list)):
        try:
            if user_list[index] + user_list[index + 1] == user_number:
                number_pair.append(user_list[index])
                number_pair.append(user_list[index + 1])
                return number_pair
        except IndexError:
            return []


# Test Code
print(sum_pairs([4, 2, 10, 5, 1], 6))
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))
print(sum_pairs([2, 4, 6, 8, 10], 14))
