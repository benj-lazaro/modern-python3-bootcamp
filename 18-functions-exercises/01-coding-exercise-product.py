# Write a function called product
# It takes two parameters
# Returns the product of the two parameters

def product(multiplicand, multiplier):
    return  multiplicand * multiplier


print("product() function")
user_multiplicand = int(input("Multiplicand: "))
user_multiplier = int(input("Multiplier: "))

print(f"{user_multiplicand} x {user_multiplier} = {product(user_multiplicand, user_multiplier)}")
