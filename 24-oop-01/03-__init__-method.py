# Define class User
class User:

    def __init__(self, first_name, last_name, age):
        # This method gets called everytime an instance of this class is created into an object
        # The self parameter refers to the individual (specific) instance of this class
        # The self parameter MUST be the first parameter to __init__(), attributes or methods on class instances
        print("A user object has been instantiated from class User.")

        # Assign the argument values into their correponding class attributes (e.g. fname, lname)
        self.fname = first_name
        self.lname = last_name
        self.age = age


# Instantiate class User into objects & password corresponding argument values
user1 = User("Joe", "Maggio", 120)
print(f"Hi there, my name is {user1.fname} {user1.lname}; {user1.age} years of age.\n")

user2 = User("Pete", "Mitchell", 56)
print(f"Hi there, my name is {user2.fname} {user2.lname}; {user2.age} years of age.\n")

user3 = User("Bob", "Garon", 100)
print(f"Hi there, my name is {user3.fname} {user3.lname}; {user3.age} years of age.\n")
