# Generator Expression
# Create generators on a single lline
# Looks somewhat like a List Comprehension except for Generators
# Uses ( ) instead of [ ]
import time

def number_sequence():
    """number_sequence() returns a generator object containing a sequence of numbers from 1 to 10."""
    for number in range(1, 10):
        yield number


# Generator object created via function
print("Generator object created from a function...")
nums = number_sequence()
print(next(nums))
print(next(nums))
print(next(nums))
print(next(nums))


# Generator object created from a Generator Expression
print("\nGenerator object created from a Generator Expression...")
print("Statement: (number for number in range(1,10))")
nums_genx = (number for number in range(1, 10) )
print(next(nums_genx))
print(next(nums_genx))
print(next(nums_genx))
print(next(nums_genx))

print("\nGenerator Expression to get the sum of the number sequence from 1 to 9...")
print("Statement: sum(number for number in range(1, 10)")
result = sum(number for number in range(1, 10))
print(f"Result: {result}")

# Measure time between generator expression and list comprehension
# Generator Expression is slightly faster than List Comprehension
# List Comprehension createa a list first then sums each item
# Genereation Expression adds each yielded number without creating a data structure (e.g. list) first

print("\nGenerator Expression x List Comprehension Time Comparison...")

print("\nGenerator Expression")
print("Statement: sum(number for number in range(1000000))")
generator_start_time = time.time()
result = sum(number for number in range(1000000))
generator_time_duration = time.time() - generator_start_time
print(f"Result: {result}")

print("\nList Comprehension")
print("Statement: sum([number for number in range(1000000)])")
list_start_time = time.time()
result = sum([number for number in range(1000000)])
list_time_duration = time.time() - list_start_time
print(f"Result: {result}")

print("\nTime Duration...")
print(f"Genereator Expression took: {generator_time_duration}")
print(f"List Comprehension took: {list_time_duration}")
