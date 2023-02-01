# Parameter = a variable in the function/method definition
# Argument  = the actual value passed into the function/method upon invocation

print("Functions with single parameter")
def square(number):
    return number * number

print(f"Square of 4: {square(4)}")
print(f"Square of 8: {square(8)}")


def sing_happy_birthday(name):
    print("Happy birthday to you!")
    print("Happy birthday to you!")
    print(f"Happy birthday dear {name}!")
    print("Happy birthday to you!")

sing_happy_birthday("Tanuki")


# Functions with multiple parameters
print("\nFunctions with multiple parameters")
def add(augend, addend):
    return augend + addend

def subtract(minued, subtrahend):
    return minued - subtrahend

def multiply(multiplicand, multiplier):
    return multiplicand * multiplier

def divide(dividend, divisor):
    return dividend / divisor

def print_full_name(first_name, last_name):
    return (f"Your full name is {first_name} {last_name}")

print(f"Sum of 50 & 50 is {add(50, 50)}")
print(f"Difference of 234 & 54 is {subtract(234, 54)}")
print(f"Product of 45 & 7 is {multiply(45, 7)}")
print(f"Quotient of 4 & 2 is {divide(4, 2)}")
print(print_full_name("Colt", "Steele"))
