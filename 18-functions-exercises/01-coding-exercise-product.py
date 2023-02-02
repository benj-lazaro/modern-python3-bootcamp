# Write a function called product
# It takes two parameters
# Returns the product of the two parameters

def product(multiplicand, multiplier):
    """product(multiplicand, multiplier) returns the product."""
    return  multiplicand * multiplier


print("Function: product()")
print(f"Documentation: {product.__doc__}")
user_multiplicand = int(input("Enter Multiplicand: "))
user_multiplier = int(input("Enter Multiplier: "))

print(f"{user_multiplicand} x {user_multiplier} = {product(user_multiplicand, user_multiplier)}")
