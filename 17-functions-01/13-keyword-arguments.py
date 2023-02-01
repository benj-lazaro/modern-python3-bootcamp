# Keyword arguments (kwargs) - only works if the parameter names are known

def full_name(first_name, last_name):
    return f"Your name is {first_name} {last_name}"

print(full_name(first_name="Colt", last_name="Steele"))
print(full_name(last_name="Steele", first_name="Colt"))


def exponent(number, power=2):
    return number ** power

print(f"3 raised to the power of 5: {exponent(number=3, power=5)}")
print(f"3 raised to the power of 2: {exponent(3)}")


