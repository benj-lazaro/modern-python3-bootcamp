# Use type() to identify if a number is an integer
print(type(9))      # Returns <class 'int'>
print(type(0.1))    # Returns <class 'float'>

# Python interpreter isn't a glorified calculator
print(1 + 4 - 2)    # Returns 3

# Calculating an integer with a floating point evaluates to a floating point
print(1 + 1.0)      # Returns a floating point 2.0
print(20 + 0.777)   # Returns a floating point 20.777
