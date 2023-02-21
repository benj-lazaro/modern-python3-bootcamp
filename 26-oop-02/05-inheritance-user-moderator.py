# Inheritance demo = model a typical permission setup of a simplified social network (e.g. reddit)
# User = typical normal user / content consumer
# Moderator = same as a user except that he/she moderates, delete/hide inappropriate posts of other users

class User:
    # Class Attribute(s)
    active_users = 0

    # Class Method(s)
    @classmethod
    def display_active_users(cls):
        """display_active_users(cls) returns a string with the value of Class Attribute active_users."""
        return f"There are currently {cls.active_users} active users."

    @classmethod
    def from_string(cls, data_string):
        """from_string(cls, string) accepts a CSV stirng, breaks it up & creates an instance of Class User."""
        first, last, age = data_string.split(",")
        return cls(first, last, int(age))

    def __init__(self, first, last, age):
        # Instance Attribute(s)
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1

    # Instance Method(s)
    def logout(self):
        """logout(self) decrements the Class Attribute active_users by 1 & returns a string."""
        User.active_users -= 1
        return f"{self.first} has logged out."

    def full_name(self):
        """full_name(self) returns the concatenated values of Instance Attributes first & last as a string."""
        return f"{self.first} {self.last}"

    def initials(self):
        """initials(self) returns the 1st character values of Instance Attributes first & last as a string."""
        return f"{self.first[0]}.{self.last[0]}."

    def likes(self, thing):
        """likes(self, thing) returns values of Instance Attributes first & thing as a string."""
        return f"{self.first} likes {self.thing}"

    def is_senior(self):
        """is_senior(self) returns a boolean value True if value of Instance Attribute age >= 65."""
        return self.age >= 65

    def birthday(self):
        """birthday(self) increments Instance Attribute age by 1 & returns a string."""
        self.age += 1
        return f"Happy {self.age}th, {self.first}"


class Moderator(User):
    # Class Attribute
    total_moderators = 0
    def __init__(self, first, last, age, community):
        # Instance Attribute(s)
        super().__init__(first, last, age)          # Access Class User's ___init__() method
        self.community = community
        Moderator.total_moderators += 1

    # Class Method(s)
    @classmethod
    def display_active_moderators(cls):
        """display_active_moderators(cls) returns a string with the value of Class Attribute tatal_moderators."""
        return f"There are currently {cls.total_moderators} active moderators."

    # Instance Method(s)
    def remove_post(self):
        """remove_post(self) returns User Instance Attribute first & Moderator Instance Attribute Moderator values."""
        return f"{self.full_name()} removed a post from the {self.community} community."


# Test Code
print("Access Class Method display_active_users() of Class User...")
print("Statemnt: User.display_active_users()")
print(User.display_active_users())

print("\nCreate 3 instances of Class User...")
user_tom = User("Tom", "Garcia", 35)
user_thomas = User("Thomas", "Acquainas", 134)
user_tomtom = User("Tom", "Thomas", 69)

print("\nAccess Class Method display_active_users() of Class User...")
print("Statemnt: User.display_active_users()")
print(User.display_active_users())

print("\nCreate 2 instances of Class Moderator...")
jasmine = Moderator("Jasmine", "Fritata", 31, "Splunking")
jamie = Moderator("Jamie", "Rivera", 55, "OPM")

print("\nAccess Class Method display_active_moderators() of Class Moderator...")
print("Statement: Moderator.display_active_moderators()")
print(Moderator.display_active_moderators())

print("\nAccess inherited Class Method display_active_users()...")
print("Statement: User.display_active_users()")
print(User.display_active_users())
