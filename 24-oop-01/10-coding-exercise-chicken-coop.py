# Define a class called Chicken
# It has an instance attribute of name (string), species (string) and eggs (int, starts at 0)
# It has an instance method called lay_egg() that:
# - Increments the instance aatribute eggs and return the current value
# _ Increments the class attribute total_eggs

class Chicken:
    # Class Attribute
    total_eggs = 0
    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.eggs = 0

    # Instance Method
    def lay_egg(self):
        """lay_egg() increments the object's eggs attribute and return the updated value."""
        Chicken.total_eggs += 1
        self.eggs += 1
        return self.eggs


chicken1 = Chicken("Alice", "Patridge Silie")
print(f"Name: {chicken1.name}")
print(f"Specifies: {chicken1.species}")
print(f"Egg Count: {chicken1.eggs}")

chicken2 = Chicken("Amelia", "Speckled Sussex")
print(f"\nName: {chicken2.name}")
print(f"Specifies: {chicken2.species}")
print(f"Egg Count: {chicken2.eggs}")

print(f"\nTotal Egg Count: {Chicken.total_eggs}\n")

print(f"{chicken1.name} laid {chicken1.lay_egg()} egg...")
print(f"{chicken2.name} laid {chicken2.lay_egg()} egg...")
print(f"{chicken2.name} laid {chicken2.lay_egg()} egg...")
print(f"{chicken1.name} laid {chicken1.lay_egg()} egg...")
print(f"Total Egg Count: {Chicken.total_eggs}\n")

print(f"Currently, {chicken1.name} has laid a total of {chicken1.eggs} egg(s).")
print(f"Currently, {chicken2.name} has laid a total of {chicken2.eggs} egg(s).")
