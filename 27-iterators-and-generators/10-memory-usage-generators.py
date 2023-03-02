# Testing memory usage with Generators demo
# Generators are easier on RAM when dealing with large sequences
# Generators are relatively slow in time

def fibonacci_list(max_value):
    """fibonacci_list(int) returns a list of fibonacci numbers."""
    number_list = []
    a , b = 0, 1

    while len(number_list) < max_value:
        number_list.append(b)
        a, b = b, a + b

    return number_list


def fibonacci_generator(max_value):
    """fibonacci_generator(int) returns a generator object of fibonacci numbers."""
    x = 0
    y = 1
    count = 0

    while count < max_value:
        x, y = y, x + y
        yield x
        count += 1

# fibonacci_list(1000000)       # Consumes roughly the entirety of the computer's RAM (8GB)
fibonacci_generator(1000000)    # Consumes RAM in the MB range

for number in fibonacci_generator(100000):
    print(number)
