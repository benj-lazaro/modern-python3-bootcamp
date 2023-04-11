# Write a function called find_factors()
# Accepts a number
# Returns a list containing all nubmers w/c are divisible by starting 1 to the passed number value


def find_factors(number_input):
    """find_factors(int) returns a list of number (i.e. factors) divisible from 1 to the passed number."""
    # NOTE: range() excludes the ending number value; need to use '+1' to include the aforementioned value
    return [number for number in range(1, number_input + 1) if number_input % number == 0]


print(find_factors(111))  # [1, 3, 37, 111 ]
print(find_factors(321421))  # [1, 293, 1097, 321421 ]
print(find_factors(412146))  # [1, 2, 3, 6, 7, 9, 14, 18, 21, 42, 63, 126, 3271, 6542, 9813, 19626, 22897,
# 29439, 45794, 58878,68691, 137382, 206073, 412146]
