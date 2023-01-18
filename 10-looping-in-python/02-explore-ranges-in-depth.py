# Range syntax with 1 parameter (end value excluded) within a for loop
print("Range() with 1 parameter:")
for x in range(10):
    print(x)

# Range syntax with 2 parameters (starting & excluded end value) within a for loop
print("Range() with 2 parameter:")
for x in range(1, 10):
    print(x)

# Range synax with 3 parameters (starting, execluded end value & step) within a for loop
print("Range() with 3 parameters:")
for x in range(1, 10, 2):
    print(x)

# Save a range of numbers in a list
print("Range of numbers from 1 to (excluded) 10, with 2 steps in-between & stored in a list:")
numbers = range(1, 10, 2)
print(list(numbers))

print("Range of numbers from 0 to (excluded) 100, with 5 steps in-between:")
for num in range(0, 100, 5):
    print(num)
