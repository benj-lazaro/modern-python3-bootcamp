# Multiple inheritance demo
class Aquatic:
    def __init__(self, name):
        print("AQUATIC INIT")
        self.name = name

    def swim(self):
        return f"{self.name} is swimming."

    def greet(self):
        return f"I am {self.name} of the sea."


class Ambulatory:
    def __init__(self, name):
        print("AMBULATORY INIT")
        self.name = name

    def walk(self):
        return f"{self.name} is walking."

    def greet(self):
        return f"I am {self.name} of the land."


class Penguin(Ambulatory, Aquatic):
    def __init__(self, name):
        print("PENGUIN INIT")
        # super().__init__(name=name)
        Ambulatory.__init__(self, name=name)  # To force call Ambulatory __init__() method
        Aquatic.__init__(self, name=name)     # To force call Aquatic class' __init__() method


# Instantiate Aquatic, Ambulatory & Penguin Classes into respective objects
# jaws = Aquatic("Jaws")
# lassie = Ambulatory("Lassie")
captain_cook = Penguin("Captain Cook")

# Access greet() method of the Penguin Class
# Access the inherited greet() method of the Ambulatory Class
# Due to THE ORDER how parent Classes are passed as PARAMETERS into the Penguin Class
print(captain_cook.greet())

# Access the inherited swim() & walk() methods of the Penguin Class
print(captain_cook.swim())
print(captain_cook.walk())

# Very inheritance of the captain_cook object
print(f"\ncaptain_cook is instance of Penguin: {isinstance(captain_cook, Penguin)}")
print(f"captain_cook is instance of Aquatic: {isinstance(captain_cook, Aquatic)}")
print(f"captain_cook is instance of Ambulatory: {isinstance(captain_cook, Ambulatory)}")
