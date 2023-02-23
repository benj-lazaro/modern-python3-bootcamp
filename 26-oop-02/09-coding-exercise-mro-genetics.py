# Create 3 classes called Mother, Father & Child
# Mother Class has attributes eye_color = "brown", hair_color = "dark brown" & hair_type = "curly"
# Father Class has attributes eye_color = "blue", hair_color = "blond" & hair_type = "straight"
# Child Class to have the same attributes but DO NOT set them on Class
# Instead use the Child Class' MRO that it inherits from Mother first then Father

class Mother:
    def __init__(self, eye_color="brown", hair_color="dark brown", hair_style="curly"):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_style = hair_style


class Father:
    def __init__(self, eye_color="blue", hair_color="blond", hair_style="straight"):
        self.eye_color = eye_color
        self.hair_color = hair_color
        self.hair_style = hair_style


class Child(Mother, Father):
    pass


print("Instantiate Mother Class into an object...")
sue = Mother()
print("Instantiate Father Class into an object...")
reed = Father()
print("Instantiate Child class into an object...")
franklin = Child()
print("Access inherited attributes of the object from Child class...")
print(f"Eye color: {franklin.eye_color}")
print(f"Hair color: {franklin.hair_color}")
print(f"Hair style: {franklin.hair_style}")
