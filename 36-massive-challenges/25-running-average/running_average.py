# Write a function called running_average()
# It returns a function
# When the returning function receives an integer value
# It returns the current average of the previous function calls
# Rounds the returning average value to the 2nd decimal place

def running_average():
    """running_average() returns the average value of passed integer values."""
    running_average_accumulator = 0
    running_average_size = 0

    def inner_function(value):
        nonlocal running_average_accumulator
        nonlocal running_average_size

        running_average_accumulator += value
        running_average_size += 1

        # For debugging purposes
        print(f"Passed Value: {value}")
        print(f"Current Value Total: {running_average_accumulator}")
        print(f"Total Passed Values: {running_average_size}")

        return round(running_average_accumulator / running_average_size, 2)

    return inner_function


# Test Code
run_average = running_average()
print(f"Average: {run_average(10)}")
print(f"Average: {run_average(20)}")
print(f"Average: {run_average(30)}")
print(f"Average: {run_average(55.5)}")
