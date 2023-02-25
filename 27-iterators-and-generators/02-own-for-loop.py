# A dumb-down custom for loop demo using iter() and next()

def my_for(iterable, func):
    """my_for(iterable, function) iterates through the iterable object & pass each item to corresponding function."""
    iterator = iter(iterable)
    while True:
        try:
            item = next(iterator)
        except StopIteration:
            break
        else:
            func(item)


def square(x):
    """square(x) prints the squared value of the passed argument."""
    print(x * x)


my_for("Hello", print)
my_for([1, 2, 3, 4, 5], square)
