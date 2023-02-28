# Generator = sub-set of an iterator
# It is a quick and short-way of creating an iterator
# It can be created with generator functions (using the keyword yield)
# It can be created with generator expressions
# It takes up less memory
# Use case: access to a value of an iterator one at a time to do something

# A generator function is a regular function except:
# - Uses the keyword yield instead of return
# - The keyword yield is used multiple time whereas keyword return is used only once
# - When invoked it returns a generator object whereas a function returns a value
# - Generator object contains only the current value; does NOT remember the previous value
# - Invokes StopIterator once the generator object's value is exhausted

def count_up_to(max_value):
    """count_up_to(int) returns the current value of generator object."""
    count = 1
    while count < max_value:
        yield count             # Returns the current value of the generator object & waits to be called via next()
        count += 1              # Increments the value of count by 1


# Test Code
# counter = count_up_to(5)
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))
# print(next(counter))          # Triggers StopIteration

counter = count_up_to(10)
next(counter)                   # Returns the generator object's current value of 1

for number in counter:
    print(number)               # Returns & prints the generator object's current value from 2 to 10
