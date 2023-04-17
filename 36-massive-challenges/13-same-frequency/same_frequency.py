# Write a function called same_frequency
# It accepts two integers
# Returns True if the numbers contain the same frequency of digits
# Otherwise, return False


def same_frequency(first_number, second_number):
    """same_frequency(int, int) return True if the occurrence of each digit from the passed integers are identical."""
    # Convert integer to string in order to be iterable; convert each character into an int
    value_one = [int(digit) for digit in str(first_number)]
    value_two = [int(digit) for digit in str(second_number)]

    # Count the occurrence of each digit from the corresponding lists
    count_one = [[item, value_one.count(item)] for item in set(value_one)]
    count_two = [[item, value_two.count(item)] for item in set(value_two)]

    # Compare for equality of occurrence
    if count_one == count_two:
        return True
    return False


# Test Code
print(same_frequency(551122, 221515))   # Returns True
print(same_frequency(321142, 3212215))  # Returns False
print(same_frequency(1212, 2211))       # Returns True
