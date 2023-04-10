# Write a function called sum_pairs
# It accepts a list (containing integers) and a separate integer
# Returns a pair of integers from the list that when summed is equivalent to the passed integer


def sum_pairs(number_list, sum_total):
    """sum_pairs(list, int) returns a list of integers whose sum is equivalent to the passed integer."""
    pair_checked = set()

    for number in number_list:
        difference = sum_total - number

        if difference in pair_checked:
            return [difference, number]
        pair_checked.add(number)

    return []


# Test Code
print("Statement: sum_pairs([4, 2, 10, 5, 1], 6)")
print(sum_pairs([4, 2, 10, 5, 1], 6))

print("Statement: sum_pairs([11, 20, 4, 2, 1, 5], 100)")
print(sum_pairs([11, 20, 4, 2, 1, 5], 100))

print("Statement: sum_pairs([2, 4, 6, 8, 10], 14)")
print(sum_pairs([2, 4, 6, 8, 10], 14))
