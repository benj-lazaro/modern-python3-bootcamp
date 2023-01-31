# Set Methods and Math
set_sample = {1, 2, 3, 4, 5}

# .add() = adds an element to a set; if it already exists, the set does NOT change
print("\nUsing .add():")
print("Add the value of 6 to the set_sample:")
print(f"set_sample: {set_sample}")
set_sample.add(6)
print(f"Result: {set_sample}")

print("\nAdd another value of 6 (duplicate) to the set_sample:")
set_sample.add(6)
print(f"Result: {set_sample}")


# .remove() = removes a value from a set; returns KeyError if value is non-existent
print("\nUsing .remove():")
print("Removes the value of 6 from the set_sample:")
set_sample.remove(6)
print(f"Result: {set_sample}")


# .discard() = removes a value from a set; does NOT return a KeyError for non-existent values
print("\nUsing .discard():")
print("Removes the value (of the non-existent) 6 from the set_sample:")
set_sample.discard(6)
print(f"Result: {set_sample}")
print("No KeyError triggered...")


# .copy() = create a copy of the set
print("\nUsing .copy():")
print("Duplicates values of set_sample to new_set")
new_set = {}
print(f"set_sample: {set_sample}")
print(f"new_set: {new_set}")
new_set = set_sample.copy()
print(f"new_set: {new_set}")
result = new_set is set_sample
print(f"Check validity of copy, if False it is a copy: {result}")


# .clear() = removes all content of a set
print("\nUsing .clear()")
print(f"Clear content of set_sample:")
print(f"set_sample: {set_sample}")
set_sample.clear()
print(f"Result: {set_sample}")


# Set Math = intersection, symmetric_difference, union
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}

# Union = return unique values of compared sets
print("\nSet Math Union (|): ")
print("Return unique values of compared sets")
print(f"biology_students: {biology_students}")
print(f"math_students: {math_students}")
result = math_students | biology_students
print(f"Result: {result}")

# Intersection = return values that exists on compared sets
print("\nSet Math Intersection (&): ")
print("Return values that exists on compared sets")
print(f"biology_students: {biology_students}")
print(f"math_students: {math_students}")
result = math_students & biology_students
print(f"Result: {result}")


