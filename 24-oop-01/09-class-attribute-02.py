# class attribute use case = keeping track of analytics, validation of input data; used within a class

class Pet:
    # Class Attribute(s)
    allowed_species = ["cat", "dog", "fish", "rat"]

    # Instance Attribute(s)
    def __init__(self, name, species):
        if species not in Pet.allowed_species:
            raise ValueError(f"You can't have a {species} pet.")
        else:
            self.name = name
            self.species = species

    def set_specifies(self, species):
        if species not in Pet.allowed_species:
            raise ValueError(f"You can't have a {species} pet.")

        self.species = species


cat = Pet("Blue", "cat")
dog = Pet("Wyatt", "dog")
print(Pet.allowed_species)
cat.allowed_species = ['tiger', 'bear']
print(f"{cat.allowed_species}")
print(f"{Pet.allowed_species}")
