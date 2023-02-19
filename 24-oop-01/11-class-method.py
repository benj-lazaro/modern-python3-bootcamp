# class methods = methods with the @classmethod decorator declared on the line prior to the class method
# They're NOT concerned with individual instances of the class but the class itself
# They're rarely implemented / used unlike instance methods
# Use case class functionality that does NOT care with instances

class User:
    # Class Attribute(s)
    active_users = 0

    # Class Method(s)
    @classmethod
    def display_active_users(cls):      # cls = class
        """display_active_users(class) returns a string regarding the number of current users."""
        return f"There are currently {cls.active_users} active users."

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
        """birthday(self) incrments the value of instance attribute age by 1 and returns a string message."""
        self.current_age += 1
        return f"Happy {self.current_age}th, {self.first_name}!"


user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)
print(User.display_active_users())

user3 = User("Yui", "Nakajima", 28)
user4 = User("Brent", "Dantes", 61)
print(User.display_active_users())
