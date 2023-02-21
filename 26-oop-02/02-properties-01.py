class Human:
    def __init__(self, first_name, last_name, current_age):
        # Instance Attribute(s)
        self.first = first_name
        self.last = last_name

        if current_age >= 0:            # Prevents from explicitly assigning a negative value upon instantiation
            self._age = current_age
        else:
            self._age = 0               # If it does, reset the Private Instance Attribute _age to 0

    def get_age(self):
        """get_age(self) returns the current value of Private Instance Attribute _age."""
        return self._age

    def set_age(self, new_age):
        """set_age(self, new_age) sets a new value of Private Instance Attribute _age."""
        if new_age >= 0:                # Prevents from explicitly assigning a negative value upon assignment
            self._age = new_age
        else:
            self._age = 0               # If it does, reset the Private Instance Attribute _age to 0



# Test Code
print("Instantiate Human Class into an object & pass initial argument values...")
print("Statment: jane = Human('Jane', 'Foster', -9)")
jane = Human("Jane", "Foster", -9)

print("\nAccess Instance Attributes first and last...")
print(f"First Name: {jane.first}")
print(f"Last Name: {jane.last}")

print("\nAccess Instance Method get_age()...")
print("Statement: jane.get_age()")
print(f"Age: {jane.get_age()}")

print("\nAccess Instance Method set_age()...")
print("Statement: jane.set_age(45)")
jane.set_age(45)
print("Statement: jane.get_age()")
print(f"Age: {jane.get_age()}")
