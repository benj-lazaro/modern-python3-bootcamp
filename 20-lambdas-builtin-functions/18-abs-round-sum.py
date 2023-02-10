# abs = returns the absolute value of a number; argument = integer or float
# sum = returns the total of the start value (default = 0) & items of an iterable (from left to right)
# round = returns a number rounded to the ndigits precision (after decimal points) else returns the nearest integer

print("abs()")
print("-----")
print("Statement: abs(3)")
print(f"Result: {abs(3)}")
print("\nStatement: abs(-3)")
print(f"Result: {abs(-3)}")
print("\nStatement: abs(3.1415)")
print(f"Result: {abs(3.1415)}")
print("\nStatement: abs(-3.1415)")
print(f"Result: {abs(-3.1415)}")

print("\nsum()")
print("-----")
number_list = [1, 2, 3, 4]
print(f"number_list: {number_list}")
print("Statement: sum(number_list)")
print(f"Result: {sum(number_list)}")

# Start value + numerical values of the iterable
print(f"\nnumber_list: {number_list}")
print("Statement: sum(number_list, 10)")
print(f"Result: {sum(number_list, 10)}")

float_list = [1.5, 2.3, 3.7]
print(f"\nfloat_list: {float_list}")
print("Statement: sum(float_list)")
print(f"Result: {sum(float_list)}")

number_set = (12, 24, 2.5)
print(f"\nnumber_set: {number_set}")
print("Statement: sum(number_set)")
print(f"Result: {sum(number_set)}")

print("\nround()")
print("-------")
print("Statement: round(3.51234)")
print(f"Result: {round(3.51234)}")

print("\nStatement: round(3.51234, None)")
print(f"Result: {round(3.51234, None)}")

print("\nStatement: round(3.51234, 2)")
print(f"Result: {round(3.51234, 2)}")

print("\nStatement: round(3.51234, 4)")
print(f"Result: {round(3.51234, 4)}")