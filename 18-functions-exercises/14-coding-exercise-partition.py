# Write a function called partition
# Accepts two parameters (a list of numbers and a callback function -> isEven())
# Callback function identifies if a number is even or odd
# Returns a list which containing truthy values (first -> even numbers) and falsy values (second -> odd numbers)

def isEven(number):
    """isEven(number) returns True if the parameter value is an even number"""
    return number % 2 == 0


def partition(list_data, callback_function):
    """partition(list, callback_function) returns a list containing truthy values first and falsy values second"""
    return [[item for item in list_data if callback_function(item) == True],
            [item for item in list_data if callback_function(item) == False]]


list_sample = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
print("Function: partition()")
print(f"Documentation: {partition.__doc__}")
print(f"list_sample: {list_sample}")
print(f"Result: {partition(list_sample, isEven)}")
