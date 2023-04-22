# Write a function called two_oldest_ages()
# It accepts a list of numbers
# Returns two of the highest numbers in the list
# The returned list should contain the 2nd highest number followed by the highest number


def two_oldest_ages(age):
    """two_oldest_ages(list) returns two of the highest numeric value in the list."""
    oldest_ages = sorted(age)
    return [oldest_ages[-2], oldest_ages[-1]]


# Test Code
print(two_oldest_ages([1, 2, 10, 8]))           # Returns [8, 10]
print(two_oldest_ages([6, 1, 9, 10, 4]))        # Returns [9,10]
print(two_oldest_ages([4, 25, 3, 20, 19, 5]))   # Returns [20,25]
