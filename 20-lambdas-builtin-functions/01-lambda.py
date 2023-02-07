# Lambda = a single-lined anonymous function

# Python normal function VS lambda function
def squared(number):
    return number * number


# Python lambdas
# Typically NOT assigned to a variable BUT can be done
squared_value = lambda number: number * number
sum_of_two_numbers = lambda a, b: a + b

print(squared(9))  # Invoke a normal function called squared
print(squared.__name__)

print(squared_value(10))  # Invoke lambda whose return value stored in variable squared_value
print(squared_value.__name__)
print(sum_of_two_numbers(1, 2))  # Invoke lambda whose return value stored in variable sum_of_two_numbers
print(sum_of_two_numbers.__name__)
