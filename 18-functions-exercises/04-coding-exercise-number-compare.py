# Write a function called number_compare
# It takes two parameters (both numbers)
# Retuns the string "First is greater" if the 1st number is greater than the 2nd
# Otherwise, returns the string "Second is greater"
# Returns the string "Numbers are equal" if both numbers are equal

def number_compare(number_1, number_2):
    """number_computer(number_1, number_2 compares two integers and returns the corresponding string description."""
    if number_1 == number_2:
        return "Numbers are equal"
    elif number_1 > number_2:
        return "First is greater"
    return "Second is greater"

print("Function: number_compare()")
print(f"Documentation: {number_compare.__doc__}")
first_number = int(input("Enter the first number: "))
second_number = int(input("Enter the second number: "))
print(f"Result: {number_compare(first_number, second_number)}")
