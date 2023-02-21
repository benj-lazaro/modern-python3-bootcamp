class Human:
    def __init__(self, first_name, last_name, current_age):
        # Instance Attribute(s)
        self.first = first_name
        self.last = last_name

        if current_age >= 0:            # Prevents from explicitly assigning a negative value upon instantiation
            self._age = current_age
        else:
            self._age = 0               # If it does, reset the Private Instance Attribute _age to 0

    # Instance Properties
    @property                           # A getter
    def age(self):                      # Treats this Instance Method like an Instance Attribute
        """age(self) returns (gets) the current value of Private Instance Attribute _age"""
        return self._age

    @age.setter                         # A setter
    def age(self, new_age):             # Treats this Instance Method like an Instance Attribute
        """age(self, new_age) sets a new value for Private Instance Attribute _age."""
        if new_age >= 0:
            self._age = new_age
        else:
            raise ValueError("Age can't be negative!")

    @property
    def fullname(self):
        """fullname(self) returns a concatenated string value taken from (get) Instance Attributes first & last."""
        return f"{self.first} {self.last}"

    @fullname.setter
    def fullname(self, name):
        """fullname(self, name) sets a new values for the Instance Attributes first & last."""
        self.first, self.last = name.split(" ")


# Test Code
print("Instantiate Human Class into an object & pass initial argument values...")
print("Statment: jane = Human('Jane', 'Foster', 29)")
jane = Human("Jane", "Foster", 29)

print("\nAccess Instance Property @property age()...")
print("Statement: jane.age")
print(f"Age; {jane.age}")

print("\nAccess Instance Property @age.setter age()...")
print("Statement: jane.age = 45")
jane.age = 45
print("Access Instance Property @property age()...")
print("Statement: jane.age")
print(f"Age: {jane.age}")

print("\nAccess Instance Prperty @property fullname()...")
print("Statement: jane.full_name")
print(f"Fullname: {jane.fullname}")

print("\nAccess Instance Prperty @fullname.setter fullname()...")
print("Statement: jane.fullname = 'Padme Amidala'")
jane.fullname = "Padme Amidala"
print("Access Instance Prperty @property fullname()...")
print("Statement: jane.full_name")
print(f"Fullname: {jane.fullname}")
print(f"First Name: {jane.first}")
print(f"Last Name: {jane.last}")
