# __repr__() = a representation dunder
# Helps provide a nicer string representation

class User:
    # Class Attribute(s)
    active_users = 0

    # Class Method(s)
    @classmethod
    def display_active_users(cls):      # cls = class
        """display_active_users(class) returns a string regarding the number of current users."""
        return f"There are currently {cls.active_users} active users."

    @classmethod
    def from_string(cls, data_string):
        """from_string(cls, str) accepts a CSV string and returns the data as a new instance of the User class."""
        first, last, age = data_string.split(",")
        return cls(first, last, int(age))   # equivalent to calling __init___() & passing in argument values

    # Instance Method(s)
    def __init__(self, first, last, age):
        # Instance Attribute(s)
        self.first_name = first
        self.last_name = last
        self.current_age = age
        User.active_users += 1

    def __repr__(self):
        """__repr__(self) returns a redadable string format with values from instance attributes."""
        return f"{self.first_name} is currently {self.current_age}."

    def full_name(self):
        """full_name() returns the user's fullname."""
        return f"{self.first_name} {self.last_name}"

    def initials(self):
        """initials(self) returns the 1st letter of the user's first and last name with a period in-between."""
        return f"{self.first_name[0]}.{self.last_name[0]}."

    def likes(self, thing):
        """likes(self, thing) returns a string regarding the user's fondness of someone or something."""
        return f"{self.first_name} likes {thing}."

    def is_senior(self):
        """is_senior(self) returns True if the user's age is greater or equal to 65; otherwise returns False."""
        return self.current_age >= 65

    def birthday(self):
        """birthday(self) increments the value of instance attribute age by 1 and returns a string message."""
        self.current_age += 1
        return f"Happy {self.current_age}th, {self.first_name}!"


joe = User.from_string("Joe,Smith,68")
blanca = User.from_string("Blanca,Lopez,41")
yui = User.from_string("Yui,Nakajima,28")
brent = User.from_string("Brent,Dantes,19")

print(joe)
print(blanca)
print(yui)
print(brent)
