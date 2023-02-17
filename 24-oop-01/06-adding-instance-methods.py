# Adding instance methods

class User:
    # Attributes
    def __init__(self, first, last, age):
        self.first_name = first
        self.last_name = last
        self.current_age = age

    # Methods
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
        self.current_age += 1
        return f"Happy {self.current_age}th, {self.first_name}!"


# Instance objects from User class
user1 = User("Joe", "Smith", 68)
user2 = User("Blanca", "Lopez", 41)

# Access instance methods
print(user1.full_name())
print(user2.full_name())

print(user1.initials())
print(user2.initials())

print(user1.likes("ice cream"))
print(user2.likes("cheetos"))

print(f"Is {user1.first_name} is a senior? {user1.is_senior()}.")
print(f"Is {user2.first_name} is a senior? {user2.is_senior()}.")

print(f"{user1.birthday()}")
print(f"{user2.birthday()}")
