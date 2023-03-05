# Speed Test Decorator
from functools import wraps
from time import time

def speed_test(func):
    """speed_test(function) performs a simple benchmarking of a function."""
    @wraps(func)
    def wrapper(*args, **kwargs):
        """wrapper(*args, **kwargs) benchmarks the passed function in terms of execution time."""
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        print(f"Executing {func.__name__}()")
        print(f"Time Elapsed: {end_time - start_time}")
        return result
    return wrapper


@speed_test
def sum_nums_generator():
    """sum_nums_genrator() returns the sum of a generator object containing numbers from 1 to 1000000."""
    return sum(number for number in range(9000000))


@speed_test
def sum_nums_list_comprehension():
    """sum_nums_list_comprehension() returns the sum of a list containing numbers from 1 to 1000000."""
    return sum([number for number in range(1000000)])


# Test Code
print(f"Operation Result: {sum_nums_generator()}\n")
print(f"Operation Result: {sum_nums_list_comprehension()}")
