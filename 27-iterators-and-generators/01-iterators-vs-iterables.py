# Iterator = an actual object that is being iterated over (a loop)
# The object returns data one element at a time when next() (behind the scene) is called on it

# Iterable = an object which returns an iterator when iter() is called on it

# Example:
# "hello" is an iterable; NOT an iterator
# iter("hello") returns an iterator

# An iterable string object assigned to a variable called name
name = "Oprah"

# Pass the iterable object to iter() to return an iterator object that is saved into the variable called iter_name
iter_name = iter(name)

# Calls next() to return the next item of the iterable object (i.e. iter_name)
# Continues to do so until a StopIterator error is raised
print(next(iter_name))
print(next(iter_name))
print(next(iter_name))
print(next(iter_name))
print(next(iter_name))
# print(next(iter_name))  # Raises a StopIterator

# Another example...
# An iterable list object is assigned to a variable called nums
nums = [1, 2, 3, 4, 5]

# Pass the iterable object into iter() to return an iterator object that is saved into the variable called iter_nums
iter_nums = iter(nums)

# Calls next() to return the next item of the iterable object (i.e. iter_nums)
# Can be repeated until a StopIterator error is raised
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))
print(next(iter_nums))
# print(next(iter_nums))  # Raises a StopIterator
