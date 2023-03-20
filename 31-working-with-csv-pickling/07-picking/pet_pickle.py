# Pickling = a way to preserve the state of data to a file in binary format
# pickle = module that serialize / deserialize a Python object into / from a byte stream
# NOTE: pickle is NOT SECURE against erroneous / maliciously constructed data from untrusted source

import pickle


class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def __repr__(self):
        return f"{self.name} is a {self.species}"


class Cat(Animal):
    def __init__(self, name, breed, toy):
        super().__init__(name, species='Cat')
        self.breed = breed
        self.toy = toy

    def play(self):
        print(f"{self.name} plays with {self.toy}")


# Instantiate class into an object
blue = Cat("Blue", "Scottish Fold", "String")

# Pickle object into a byte stream called pet.pickle
with open("pet.pickle", "wb") as data:
    pickle.dump(blue, data)

# Unpickle the byte stream pet.pickle into readable content
with open("pet.pickle", "rb") as data:
    zombie_blue = pickle.load(data)

    print(zombie_blue)
    zombie_blue.play()
