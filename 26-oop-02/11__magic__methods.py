# magic methods = user defined methodsd that can mimic the behavior of built-in objects
from copy import copy

class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age

    def __repr__(self):
        """__repr__() returns a string containing the value of Instance Attributes first & last."""
        return f"A human named {self.first} {self.last} aged {self.age}."

    def __len__(self):
        """__len__() returns the value of Instance Attribute age."""
        return self.age

    def __add__(self, other):
        if isinstance(other, Human):
            return Human(first="newborn", last=self.last, age=0)
        return "You can't add that!"

    def __mul__(self, other):
        if isinstance(other, int):
            return [copy(self) for i in range(other)]   # Use copy() to create a separate copy of self
        return "Can't multiply"

print("Instantiate Class Human into objects...")
redhood = Human("Jason", "Todd", 45)
batgirl = Human("Barbara", "Gordon", 48)

print("\nAccess objects' __repr__() method...")
print(redhood)
print(batgirl)

print("\nAccess objects' __len__() method...")
print(len(redhood))
print(len(batgirl))

print("\nAccess objects' __add__() method...")
baby_todd = redhood + batgirl
print(baby_todd)

print("\nAccess objects' __mul__() method...")
triplets = redhood * 3      # Multiply (clone) the object redhood 3 times using __mul__() & save it to a list
print(triplets)

triplets[1].first = "Jay"
print(triplets)

print("\nAccess object's __add__() & __mul__() methods...")
children = (redhood + batgirl) * 3
children[0].first = "Cassie"
children[1].first = "Jimmy"
children[2].first = "Barbie"
print(children)
