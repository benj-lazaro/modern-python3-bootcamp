# class attributes = defined once on the class; shared by all instances of a class & the class itself

class User:
    # Class attribute(s)
    active_users = 0

    # Instance Attribute(s)
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.current_age = age
        User.active_users += 1

    # Instance Method(s)
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
        """birthday(self) increments user's age by 1 and returns a birthday greeting message."""
        self.current_age += 1
        return f"Happy {self.current_age}th, {self.first_name}!"

    def logout(self):
        """logout(self) decrements class attribute active_users by 1 & returns a message."""
        User.active_users -= 1
        return f"{self.first_name} logged out."



print(f"Active Users: {User.active_users}")

print("\nInstantiate two objects from class User....")
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

print(f"Active Users: {User.active_users}")

print("\nUser Blance logs out from the system...")
print(f"{user2.logout()}")
print(f"Active Users: {User.active_users}")
