# Write a function called get_unlimited_multiples
# Accepts a number
# Returns a generator that yield an unlimited number of multiples of that number
# Default value of number is 1

def get_unlimited_multiples(number=1):
    """get_unlimited_multiples(int) returns a generator object containing infinite multiples of passed number."""
    current_number = number

    while True:
        yield current_number
        current_number += number


# Test Code
# Generate a list of 15 items; each item is a multiple of the passed argument value
print("Generate a list of 15 items...")
print("Each item is a multiple of the passed argument value (whose default value is 1)...")
generator_object = get_unlimited_multiples(7)
result = [next(generator_object) for index in range(15)]
print(result)

generator_object = get_unlimited_multiples(2)
result = [next(generator_object) for index in range(15)]
print(result)

generator_object = get_unlimited_multiples()
result = [next(generator_object) for index in range(15)]
print(result)