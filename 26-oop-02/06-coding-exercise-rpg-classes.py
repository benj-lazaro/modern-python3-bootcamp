# Define a base class called Character
# It will contain the following properties: name (string), hp (int), level (int)

class Character():
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level


# Define a subclass of Character called NPC
# It has an additional instance method called speak()
class NPC(Character):
    def __init__(self, name, hp, level):
        super().__init__(name, hp, level)

    def speak(self):
        """speak(self) simply returns a string."""
        return "I heard there were monsters running around last night!"


# Test Code
print("Create an instance of the Child Class NPC...")
npc_villager = NPC("Bob Baker", 100, 1)

print("\nAccess Instance Attributes name, hp and level")
print(f"NPC Name: {npc_villager.name}")
print(f"NPC HP Level: {npc_villager.hp}")
print(f"NPC Experience Level: {npc_villager.level}")
print(f"NPC {npc_villager.name} says '{npc_villager.speak()}'.")
