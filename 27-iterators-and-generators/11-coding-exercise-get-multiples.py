# Write a functionca called get_multiples
# Accepts a number and count (both int)
# Returns a generator object that yields the first count multiples of the number
# Default value of number is 1
# Default value of count is 10

def get_multiples(number=1, count=10):
    """get_multiples(int, int) returns a generator object containing finite multiples of passed number."""
    for index in range(1, count + 1):
        yield number * index


num = get_multiples(2, 3)
print(next(num))
print(next(num))
print(next(num))

