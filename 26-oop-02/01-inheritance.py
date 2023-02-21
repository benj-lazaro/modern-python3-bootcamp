# OOP inheritance demo

# Base / Parent class
class Animal():
    # Class Attribute(s)
    cool = True

    # Instance Method(s)
    def make_sound(self, sound):
        print(f"This animal says {sound}")


# Child class
class Cat(Animal):  # Inherits Animal class attributes & methods by passing the class name as an argument value
    pass


print("Instantiate parent class Animal...")
generic_animal = Animal()           # Instantiate parent class Animal
generic_animal.make_sound("chirp")  # Access instance method make_sound()
print(Animal.cool)                  # Access class attribute cool

print("\nInstantiate child class Cat...")
gandalf = Cat()                     # Instantiate child class Cat
gandalf.make_sound("meow")          # Access inherited instance method make_sound()
print(gandalf.cool)                 # Access inherited class attribute cool

print("\nVerify inheritance of an object using isistance()...")
print(f"Is object gandalf an instance of class Cat: {isinstance(gandalf, Cat)}")
print(f"Is object gandalf an instance of class Animal: {isinstance(gandalf, Animal)}")
print(f"Is object gandalf an instance of class object: {isinstance(gandalf, object)}")