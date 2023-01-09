# Demonstration on is VS == operators
a = [1, 2, 3]
b = [1, 2, 3]

expression = a == b     # Check for identical values
print(expression)

expression = a is b
print(expression)       # Identical values but stored on different memory locations

c = b
expression = b is c
print(expression)       # Identical values & memory locations

