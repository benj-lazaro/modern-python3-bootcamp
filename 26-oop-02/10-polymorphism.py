# polymorphism demo
# An Object can take on many (poly) forms (morph)
# Same Class Method works in a similar way for different Classes
# Common implementation -> a Method in the Parent Class that is overriden by a Sub-Class (i.e. Method Overriding)
# Each Sub-Class will have different implementation of the Method

class Animal:
    def speak(self):
        raise NotImplementedError("Sub-class needs to implement this method.")

class Dog(Animal):
    def speak(self):
        return "Woof!"

class Cat(Animal):
    def speak(self):
        return "Meow!"

class Fish(Animal):
    pass


print("Polymorphism #1: Same Class Method works in a similar way for different Classes.")
dog = Dog()
cat = Cat()
fish = Fish()
print("Calling the same Instance Method speak() from on different Sub-Classes ")
print(dog.speak())
print(cat.speak())
# print(fish.speak())     # Triggers NotImplementedError


# Same operation works for different kinds of Objects
sample_list = [1, 2, 3]
sample_tuple = (1, 2, 3)
sample_string = "awesome"

print("\nPolymorphism #2: Same operation works for different kinds of objects.")
print(f"sample_list: {sample_list}")
print("Statement: len(sample_list)")
print(f"Result: {len(sample_list)}")

print(f"sample_tuple: {sample_tuple}")
print("Statement: len(sample_tuple)")
print(f"Result: {len(sample_tuple)}")

print(f"sample_string: {sample_string}")
print("Statement: len(sample_string)")
print(f"Result: {len(sample_string)}")
