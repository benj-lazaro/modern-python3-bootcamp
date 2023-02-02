# Write a function called multiply_even_numbers
# Accepts 1 parameter (list of numbers)
# Returns the product of all even numbers in the list

def multiply_even_numbers(list_data):
    """mutiply_even_numbers(lists) returns the product of all even numbers in the list."""
    product = 1

    for number in list_data:
        if number % 2 == 0:
            product *= number

    return product

list_number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Function: multiply_even_number()")
print(f"Documentation: {multiply_even_numbers.__doc__}")
print(f"list_number: {list_number}")
print(f"Product: {multiply_even_numbers(list_number)}")
