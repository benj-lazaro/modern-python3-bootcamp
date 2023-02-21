# super() method demo
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}."

    def make_sound(self, sound):
        print(f"This animal says {sound}")

class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species="Cat")   # Call Animal class' ___init__(); no need to pass self (Cat) as argument
        self.breed = breed
        self.toy = toy

    def play(self):
        """play(self) returns a string containing value of Instance Attribute toy."""
        print(f"{self.name} plays with {self.toy}.")


print("Instantiate child class Cat into an object...")
print("Statement: blue = Cat('Blue', 'Cat', 'Scottish Fold', 'String')")
blue = Cat("Blue", "Scottish Fold", "String")

print("\nAccess inherited __repr__() of Animal Class....")
print("Statement: print(blue)")
print(blue)

print("\nAccess inherited Instance Attributes name & species of Animal Class c/o super()...")
print("Statement: blue.name")
print("Statement: blue.species")
print(f"{blue.name}'s species is {blue.species}")

print("\nAccess Instance Attribute breed of Cat Class...")
print("Statement: blue.breed")
print(f"{blue.name}'s breed is {blue.breed}")

print("\nAccess Instance Method play() of Cat Class...")
print("Statement: blue.play()")
blue.play()
