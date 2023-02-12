# Write a function called divide
# Accepts two parameters (numbers)
# Returns a custom error message for TypeError
# Returns a custom error message for ZeroDivision
# Returns the quotient value

def divide(divident, divisor):
    try:
        quotient = divident / divisor
    except TypeError:
        return "Please provide two integer or float values."
    except ZeroDivisionError:
        return "Please do not divide by zero."
    else:
        return quotient


print(divide(4, 2))
print(divide([],"1"))   # Triggers a TypeError
print(divide(1,0))      # Triggers a ZeroDivisionError
