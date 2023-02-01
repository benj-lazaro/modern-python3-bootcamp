# Basic syntax of default parameters

# Function with default parameter power = 2
def exponent(number, power=2):
    return number ** power


# Test function with default & different argument values
print("Function with default parameter power = 2:")
print(f"Exponent of 2 ^3: {exponent(2, 3)}")
print(f"Exponent of 3 ^2: {exponent(3, 2)}")
print(f"Exponent of 5 ^2: {exponent(5)}")
print(f"Exponent of 3 ^5: {exponent(3, 5)}")


print("\nFunction with default parameters first_name and is_instructor:")
def show_information(first_name="Colt", is_instructor=False):
    if first_name == "Colt" and is_instructor:
        return f"Welcome back instructor Colt!"
    elif first_name == "Colt":
        return "I really thought you were an instructor..."
    return f"Hello {first_name}"

print(show_information())
print(show_information(is_instructor=True))
print(show_information('Molly'))


print("\nFunction with default parameter math_operation")
def add(augend, addend):
    return augend + addend

def subtract(minued, subtrahend):
    return minued - subtrahend

def math(first_number, second_number, math_operation=add):
    return math_operation(first_number, second_number)

print(f"1 + 10 = {math(1, 10)}")
print(f"2 +  2 = {math(2, 2, add)}")
print(f"2 -  2 = {math(2, 2, subtract)}")
