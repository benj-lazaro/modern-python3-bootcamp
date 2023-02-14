# Write function called lucky_number & save it on helpers.py
# The function returns the number 37
# Import helpers.py in this file and call the funttion lucky_number
# Save the returned value to a variable called num

import helpers

print("Calling lucky_number() of the module helpers...")
print(f"Documentation: {helpers.lucky_number.__doc__}")

print("Statement: helpers.lucky_number()")
num = helpers.lucky_number()
print(f"Result: {num}")
