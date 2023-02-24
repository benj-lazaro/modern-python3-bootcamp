# Create a class called Train
# It has 1 attribute called num_cars w/c is specified when instantiated
# It has 2 magic methods __repr__() and __len__()

class Train:
    def __init__(self, num_cars):
        # Instance Attribute(s)
        self.cars = num_cars

    # Instance Method(s)
    def __repr__(self):
        """__repr__(self) returns a string containing the value of self.cars."""
        return f"{self.cars} car train"

    def __len__(self):
        """__len__(self) returns the value of self.cars."""
        return self.cars


# Test Code
print("Instantiate Train Class into an object...")
print("Statement: the_a_train = Train(4)")
the_a_train = Train(4)

print("\nAccess the __repr__() method of the object...")
print("Statement: the_a_train")
print(the_a_train)

print("\nAccess the __len__() method of the object...")
print("Statement: len(the_a_train)")
print(len(the_a_train))
